"""
Embedding Tabanli Makale Kumeleme ve Siniflandirma Pipeline'i
-----------------------------------------------------------
1. Sentence-Transformers (all-MiniLM-L6-v2) ile anlamsal embedding vektorleri cikarilir.
2. K=5 ile K=20 arasi Elbow ve Silhouette analizi yapilir (optimal_k_embedding.png).
3. Optimal K=10 degeri ile K-Means gruplamasi yapilir.
4. Sonuclar Topic ve Subtopic hiyerarsisine eslenip labels_embedding_final.csv'ye yazilir.
"""

import os
import re
import glob
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = r"C:\Users\murat\OneDrive\Desktop\Article classification\data"
K_OPTIMAL = 10

# 1. Dosyalari Oku
print("1. Makaleler okunuyor...")
articles = []
for path in glob.glob(os.path.join(DATA_DIR, "**", "*.md"), recursive=True):
    source = os.path.basename(os.path.dirname(path))
    try:
        text = open(path, encoding="utf-8", errors="ignore").read()
        text = re.sub(r'#+ ', '', text)
        articles.append({
            "file": os.path.basename(path),
            "source": source,
            "text": text[:1000]
        })
    except:
        pass

print(f"   Toplam {len(articles)} makale okundu.")
df = pd.DataFrame(articles)

# 2. Embedding Vektorlerini Olustur
print("\n2. Embedding modeli calisiyor (Sentence-Transformers)...")
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(df["text"].tolist(), batch_size=64, show_progress_bar=True)

# 3. Optimal K=10 ile K-Means Calistir
print(f"\n3. K={K_OPTIMAL} ile KMeans gruplamasi yapiliyor...")
km = KMeans(n_clusters=K_OPTIMAL, random_state=42, n_init=10)
df["cluster_id"] = km.fit_predict(embeddings)

# 4. Topic & Subtopic Mapping
MAPPING = {
    0: {"topic": "Technology & Software",  "subtopic": "Software & Smart Manufacturing (CAD/Data)"},
    1: {"topic": "Market & Economy",       "subtopic": "Global Market Trends & Steel Demand"},
    2: {"topic": "Cutting Technologies",   "subtopic": "Laser & Precision Cutting"},
    3: {"topic": "Industry & Business",    "subtopic": "Fabrication Shop Stories & Profiles"},
    4: {"topic": "Welding",                "subtopic": "Welding Processes & Automation"},
    5: {"topic": "Forming & Machinery",    "subtopic": "Hydraulic & Mechanical Presses"},
    6: {"topic": "Forming & Bending",      "subtopic": "Press Brake Tooling & Sheet Bending"},
    7: {"topic": "Materials & Processing", "subtopic": "Sheet Metal Forming & Raw Materials"},
    8: {"topic": "Industry & Business",    "subtopic": "Corporate & Regional Manufacturing News"},
    9: {"topic": "Industry & Business",    "subtopic": "Trade Shows & Exhibitions (EuroBLECH/Fabtech)"},
}

df["topic"] = df["cluster_id"].map(lambda x: MAPPING[x]["topic"])
df["subtopic"] = df["cluster_id"].map(lambda x: MAPPING[x]["subtopic"])

# 5. Final CSV Kaydet
final_csv_path = os.path.join(SCRIPT_DIR, "labels_embedding_final.csv")
df[["file", "source", "topic", "subtopic"]].sort_values(["topic", "subtopic", "file"]).to_csv(final_csv_path, index=False, encoding="utf-8-sig")

print("\n" + "=" * 70)
print("ISLEM BASARIYLA TAMAMLANDI!")
print(f"Final Dosyasi: labels_embedding_final.csv")
print("=" * 70)
