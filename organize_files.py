import os
import shutil
import glob
import pandas as pd

# 1. Dosya Yollari ve Ayarlar
CSV_FILE = "labels_final.csv"
DATA_DIR = r"C:\Users\murat\OneDrive\Desktop\StajProje\data"
OUTPUT_DIR = r"C:\Users\murat\OneDrive\Desktop\StajProje\organized_data"

print("1. labels_final.csv okunuyor...")
df = pd.read_csv(CSV_FILE)

# Klasör isimlerinde geçersiz karakterler varsa temizle (örn: /, \, :, *, ?, ", <, >, |)
def clean_folder_name(name):
    invalid_chars = r'<>:"/\|?*'
    for char in invalid_chars:
        name = name.replace(char, "_")
    return name.strip()

print("2. Ham verideki tum .md dosyalarinin yollari indexleniyor...")
file_index = {}
for path in glob.glob(os.path.join(DATA_DIR, "**", "*.md"), recursive=True):
    fname = os.path.basename(path)
    file_index[fname] = path

print(f"   Toplam {len(file_index)} fiziki dosya indekslendi.\n")

print("3. Dosyalar Topic -> Subtopic klasorlerine kopyalaniyor...")

copied_count = 0
missing_count = 0

for idx, row in df.iterrows():
    filename = row["file"]
    topic = clean_folder_name(str(row["topic"]))
    subtopic = clean_folder_name(str(row["subtopic"]))
    
    # Hedef klasor yolu: organized_data/Topic/Subtopic/
    target_folder = os.path.join(OUTPUT_DIR, topic, subtopic)
    os.makedirs(target_folder, exist_ok=True)
    
    # Kaynak dosya yolu
    source_path = file_index.get(filename)
    
    if source_path and os.path.exists(source_path):
        target_path = os.path.join(target_folder, filename)
        shutil.copy2(source_path, target_path)
        copied_count += 1
    else:
        missing_count += 1

    if (idx + 1) % 5000 == 0 or (idx + 1) == len(df):
        print(f"   {idx + 1} / {len(df)} dosya islendi...")

print("\n" + "=" * 70)
print("ISLEM TAMAMLANDI! 🎉")
print(f"✅ Basariyla kopyalanan dosya: {copied_count}")
if missing_count > 0:
    print(f"⚠️ Bulunamayan dosya: {missing_count}")
print(f"📁 Dosyalariniz su adreste duzenlendi: {OUTPUT_DIR}")
print("=" * 70)
