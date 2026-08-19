import os
import re
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # GUI olmadan çalışsın
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# 1. Dosyaları oku
DATA_DIR = r"C:\Users\murat\OneDrive\Desktop\StajProje\data"

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

print(f"Toplam makale: {len(articles)}")

df = pd.DataFrame(articles)

# 2. TF-IDF
vectorizer = TfidfVectorizer(max_features=500, stop_words="english", min_df=2)
X = vectorizer.fit_transform(df["text"])

# 3. Farklı cluster sayılarını dene (5-25 arası)
K_range = range(5, 26)
inertias = []
silhouettes = []

print("\nCluster sayıları deneniyor...\n")
for k in K_range:
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = model.fit_predict(X)
    inertias.append(model.inertia_)
    sil = silhouette_score(X, labels, sample_size=5000, random_state=42)
    silhouettes.append(sil)
    print(f"  K={k:2d}  |  Silhouette: {sil:.4f}")

# 4. Grafik çiz
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Elbow grafiği
ax1.plot(K_range, inertias, 'bo-')
ax1.set_xlabel('Cluster Sayisi (K)')
ax1.set_ylabel('Inertia')
ax1.set_title('Elbow Method - En iyi K nerede dirsek yapar?')
ax1.grid(True)

# Silhouette grafiği
ax2.plot(K_range, silhouettes, 'ro-')
ax2.set_xlabel('Cluster Sayisi (K)')
ax2.set_ylabel('Silhouette Score')
ax2.set_title('Silhouette Score - Yuksek olan daha iyi')
ax2.grid(True)

best_k = list(K_range)[silhouettes.index(max(silhouettes))]
ax2.axvline(x=best_k, color='green', linestyle='--', label=f'En iyi K={best_k}')
ax2.legend()

plt.tight_layout()
plt.savefig("optimal_k.png", dpi=150)
print(f"\nEn iyi K = {best_k} (Silhouette = {max(silhouettes):.4f})")
print("Grafik kaydedildi: optimal_k.png")
