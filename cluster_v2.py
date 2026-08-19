import os
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# 1. Dosyaları oku
DATA_DIR = r"C:\Users\murat\OneDrive\Desktop\StajProje\data"
NUM_SUBTOPICS = 15

articles = []
for root, dirs, files in os.walk(DATA_DIR):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)
            source = os.path.basename(root)
            try:
                text = open(path, encoding="utf-8", errors="ignore").read()
                text = re.sub(r'#+ ', '', text)
                articles.append({"file": file, "source": source, "text": text, "path": path})
            except:
                pass

print(f"Toplam makale: {len(articles)}")

df = pd.DataFrame(articles)

# 2. TF-IDF
vectorizer = TfidfVectorizer(max_features=500, stop_words="english", min_df=2)
X = vectorizer.fit_transform(df["text"])
terms = vectorizer.get_feature_names_out()

# 3. KMeans ile 15 subtopic oluştur
model = KMeans(n_clusters=NUM_SUBTOPICS, random_state=42, n_init=10)
df["subtopic_id"] = model.fit_predict(X)

# 4. Her subtopic'in en belirgin kelimelerini bul
print("\n" + "="*70)
print("SUBTOPIC'LER VE EN BELİRGİN KELİMELERİ")
print("="*70)

subtopic_info = {}
for i in range(NUM_SUBTOPICS):
    center = model.cluster_centers_[i]
    top_words = [terms[j] for j in center.argsort()[-8:][::-1]]
    count = (df["subtopic_id"] == i).sum()
    subtopic_info[i] = {"words": top_words, "count": count}
    print(f"\n  Subtopic {i:2d} ({count:5d} makale)")
    print(f"    Kelimeler: {', '.join(top_words)}")

# 5. Benzer subtopic'leri ana topic altında grupla
# Bu mapping'i elle yapıyoruz - kelimelere bakarak
# Şimdilik subtopic'leri olduğu gibi kaydedelim, topic mapping'i sonra ekleyeceğiz

# Subtopic isimleri oluştur (en belirgin 3 kelimeden)
subtopic_names = {}
for i, info in subtopic_info.items():
    subtopic_names[i] = " & ".join(info["words"][:3]).title()

df["subtopic"] = df["subtopic_id"].map(subtopic_names)

# 6. CSV kaydet
output = df[["file", "source", "subtopic_id", "subtopic"]].copy()
output = output.sort_values(["subtopic_id", "file"])
output.to_csv("labels_v2.csv", index=False)

print(f"\n{'='*70}")
print(f"Kaydedildi: labels_v2.csv")
print(f"Toplam: {len(df)} makale, {NUM_SUBTOPICS} subtopic")

# 7. Özet tablo
print(f"\n{'='*70}")
print("ÖZET: Her subtopic'te kaç makale var?")
print("="*70)
summary = df.groupby(["subtopic_id", "subtopic"]).size().reset_index(name="count")
summary = summary.sort_values("subtopic_id")
for _, row in summary.iterrows():
    bar = "█" * (row["count"] // 100)
    print(f"  {row['subtopic_id']:2d} | {row['count']:5d} | {bar} {row['subtopic']}")
