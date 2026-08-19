import os
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# 1. Tüm .md dosyalarını oku
DATA_DIR = r"C:\Users\murat\OneDrive\Desktop\StajProje\data"
NUM_TOPICS = 10  # kaç ana konu olsun (sonra ayarlarız)

articles = []
for root, dirs, files in os.walk(DATA_DIR):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)
            source = os.path.basename(root)
            try:
                text = open(path, encoding="utf-8", errors="ignore").read()
                # Markdown # işaretlerini temizle
                text = re.sub(r'#+ ', '', text)
                articles.append({"file": file, "source": source, "text": text})
            except:
                pass

print(f"Toplam makale: {len(articles)}")

# 2. TF-IDF ile metinleri sayıya çevir
df = pd.DataFrame(articles)
vectorizer = TfidfVectorizer(max_features=500, stop_words="english", min_df=2)
X = vectorizer.fit_transform(df["text"])

# 3. KMeans ile grupla
model = KMeans(n_clusters=NUM_TOPICS, random_state=42, n_init=10)
df["topic_id"] = model.fit_predict(X)

# 4. Her grubun en belirgin kelimelerini bul (konu adı olarak kullan)
terms = vectorizer.get_feature_names_out()
topic_names = {}
for i in range(NUM_TOPICS):
    center = model.cluster_centers_[i]
    top_words = [terms[j] for j in center.argsort()[-5:][::-1]]
    topic_names[i] = "_".join(top_words)
    print(f"Topic {i}: {', '.join(top_words)}")

df["topic"] = df["topic_id"].map(topic_names)

# 5. CSV olarak kaydet
df[["file", "source", "topic"]].to_csv("labels.csv", index=False)
print("\nBitti! labels.csv oluşturuldu.")