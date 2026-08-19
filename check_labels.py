import pandas as pd, os, random, glob

random.seed(42)
df = pd.read_csv("labels_final.csv")
DATA_DIR = r"C:\Users\murat\OneDrive\Desktop\StajProje\data"

# Tum dosyalarin tam yollarini indexle
file_index = {}
for path in glob.glob(os.path.join(DATA_DIR, "**", "*.md"), recursive=True):
    fname = os.path.basename(path)
    file_index[fname] = path

topics = sorted(df["topic"].unique())

for t in topics:
    sub = df[df["topic"] == t]
    row = sub.sample(1, random_state=random.randint(0, 999)).iloc[0]
    
    filepath = file_index.get(row["file"], None)
    if filepath:
        lines = open(filepath, encoding="utf-8", errors="ignore").readlines()[:8]
        preview = "".join(lines).strip()[:400]
    else:
        preview = "(dosya bulunamadi)"
    
    print("=" * 70)
    print(f"  TOPIC:    {t}")
    print(f"  SUBTOPIC: {row['subtopic']}")
    print(f"  FILE:     {row['file']}")
    print(f"  ICERIK:")
    print(f"  {preview}")
    print()
