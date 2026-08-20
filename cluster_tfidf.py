"""
TF-IDF Tabanli Makale Kumeleme ve Siniflandirma Pipeline'i
-----------------------------------------------------------
1. TF-IDF yontemi ile kelime bazli analiz yapilir.
2. K=15 ile K-Means gruplamasi yapilir.
3. Sonuclar Topic ve Subtopic hiyerarsisine eslenip labels_final.csv'ye yazilir.
"""

import os
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "data")
NUM_SUBTOPICS = 15

# 1. Dosyalari Oku
print("1. Makaleler okunuyor...")
articles = []
for root, dirs, files in os.walk(DATA_DIR):
    for file in files:
        if file.endswith(".md"):
            path = os.path.join(root, file)
            source = os.path.basename(root)
            try:
                text = open(path, encoding="utf-8", errors="ignore").read()
                text = re.sub(r'#+ ', '', text)
                articles.append({"file": file, "source": source, "text": text})
            except:
                pass

print(f"   Toplam {len(articles)} makale okundu.")
df = pd.DataFrame(articles)

# 2. TF-IDF
print("\n2. TF-IDF kelime matrisi olusturuluyor...")
vectorizer = TfidfVectorizer(max_features=500, stop_words="english", min_df=2)
X = vectorizer.fit_transform(df["text"])

# 3. K-Means
print(f"\n3. K={NUM_SUBTOPICS} ile KMeans gruplamasi yapiliyor...")
model = KMeans(n_clusters=NUM_SUBTOPICS, random_state=42, n_init=10)
df["subtopic_id"] = model.fit_predict(X)

# 4. Topic & Subtopic Mapping
MAPPING = {
    0: {"topic": "Market & Economy",         "subtopic": "Global Market Trends"},
    1: {"topic": "Cutting Technologies",     "subtopic": "Waterjet & Plasma Cutting"},
    2: {"topic": "Design & Engineering",     "subtopic": "CAD & 3D Modeling"},
    3: {"topic": "Cutting Technologies",     "subtopic": "Laser Cutting"},
    4: {"topic": "Forming & Bending",        "subtopic": "General Machinery & Tube Bending"},
    5: {"topic": "Materials",                "subtopic": "Steel & Raw Materials"},
    6: {"topic": "Forming & Bending",        "subtopic": "Press Brake & Hydraulic Systems"},
    7: {"topic": "Industry & Business",      "subtopic": "US Fabrication News (FMA/Fabtech)"},
    8: {"topic": "Industry & Business",      "subtopic": "Company Profiles & Stories"},
    9: {"topic": "Industry & Business",      "subtopic": "Trade Shows & Exhibitions"},
    10: {"topic": "Welding",                 "subtopic": "Welding Processes & Robotics"},
    11: {"topic": "Forming & Bending",       "subtopic": "Bending Tooling & Die Design"},
    12: {"topic": "Industry & Business",     "subtopic": "General Manufacturing & Production"},
    13: {"topic": "Industry & Business",     "subtopic": "UK Manufacturing Sector"},
    14: {"topic": "Cutting Technologies",    "subtopic": "Surface Treatment & Plasma Tables"},
}

df["topic"] = df["subtopic_id"].map(lambda x: MAPPING[x]["topic"])
df["subtopic"] = df["subtopic_id"].map(lambda x: MAPPING[x]["subtopic"])

# 5. Final CSV Kaydet
final_csv_path = os.path.join(SCRIPT_DIR, "labels_final.csv")
output = df[["file", "source", "topic", "subtopic"]].copy()
output.sort_values(["topic", "subtopic", "file"]).to_csv(final_csv_path, index=False, encoding="utf-8-sig")

print("\n" + "=" * 70)
print("ISLEM BASARIYLA TAMAMLANDI!")
print(f"Final Dosyasi: labels_final.csv")
print("=" * 70)
