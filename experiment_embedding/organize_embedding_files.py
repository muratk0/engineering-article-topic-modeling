import os
import glob
import shutil
import pandas as pd
from tqdm import tqdm

BASE_DIR = r"C:\Users\murat\OneDrive\Desktop\Article classification"
DATA_DIR = os.path.join(BASE_DIR, "data")
CSV_PATH = os.path.join(BASE_DIR, "experiment_embedding", "labels_embedding_final.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "organized_embedding_data")

def sanitize_folder_name(name):
    """Windows klasor isimlerinde sorun yaratan karakterleri temizler."""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        name = name.replace(char, '-')
    return name.strip()

print("1. Orijinal dosyalarin yerleri bulunuyor...")
file_paths = {}
for path in glob.glob(os.path.join(DATA_DIR, "**", "*.md"), recursive=True):
    fname = os.path.basename(path)
    source = os.path.basename(os.path.dirname(path))
    file_paths[(fname, source)] = path

print("2. CSV dosyasi okunuyor...")
df = pd.read_csv(CSV_PATH)

print(f"3. '{OUTPUT_DIR}' klasorune makaleler kopyalaniyor...")
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Hata veya kopyalanan sayisini tutalim
copied_count = 0
error_count = 0

for idx, row in df.iterrows():
    fname = row["file"]
    source = row["source"]
    topic = sanitize_folder_name(row["topic"])
    subtopic = sanitize_folder_name(row["subtopic"])
    
    orig_path = file_paths.get((fname, source))
    
    if orig_path:
        # Yeni hedef klasoru olustur
        dest_folder = os.path.join(OUTPUT_DIR, topic, subtopic)
        os.makedirs(dest_folder, exist_ok=True)
        
        # Dosyayi hedefe kopyala
        dest_path = os.path.join(dest_folder, fname)
        try:
            shutil.copy2(orig_path, dest_path)
            copied_count += 1
        except Exception as e:
            error_count += 1
    else:
        error_count += 1

print("\n" + "=" * 50)
print("KOPYALAMA ISLEMI TAMAMLANDI!")
print(f"Olusturulan Klasor: {OUTPUT_DIR}")
print(f"Basariyla kopyalanan: {copied_count}")
print(f"Bulunamayan/Hata: {error_count}")
print("=" * 50)
