import os
import pandas as pd

BASE_DIR = r"C:\Users\murat\OneDrive\Desktop\Article classification"
DATA_DIR = os.path.join(BASE_DIR, "data")

df_tfidf = pd.read_csv(os.path.join(BASE_DIR, "labels_final.csv"))
df_embed = pd.read_csv(os.path.join(BASE_DIR, "experiment_embedding", "labels_embedding_final.csv"))

merged = pd.merge(df_tfidf, df_embed, on=["file", "source"], suffixes=("_tfidf", "_embed"))
merged = merged.drop_duplicates(subset=["file", "source"])

sample = merged.sample(15, random_state=123)

print("="*80)
print("TF-IDF vs EMBEDDING - RASTGELE MAKALE SAGLAMASI")
print("="*80)

for idx, row in sample.iterrows():
    fname = row['file']
    source = row['source']
    
    file_path = None
    for root, _, files in os.walk(DATA_DIR):
        if fname in files and os.path.basename(root) == source:
            file_path = os.path.join(root, fname)
            break
            
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read().replace("\n", " ").strip()
                text = text[:300]
                
            print(f"\n[DOSYA] {fname}")
            print(f"ICERIK : {text}...")
            print(f"TF-IDF : [{row['topic_tfidf']}] -> {row['subtopic_tfidf']}")
            print(f"EMBED  : [{row['topic_embed']}] -> {row['subtopic_embed']}")
            
        except Exception as e:
            print(f"Hata okuma: {e}")

print("\n" + "="*80)
