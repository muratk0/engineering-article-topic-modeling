import pandas as pd

# labels_v2.csv'yi oku
df = pd.read_csv("labels_v2.csv")

# Subtopic ID -> anlamli isim ve ana topic mapping
MAPPING = {
    # TOPIC: Cutting & Laser
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

# Mapping uygula
df["topic"] = df["subtopic_id"].map(lambda x: MAPPING[x]["topic"])
df["subtopic"] = df["subtopic_id"].map(lambda x: MAPPING[x]["subtopic"])

# Final CSV kaydet
output = df[["file", "source", "topic", "subtopic"]].copy()
output = output.sort_values(["topic", "subtopic", "file"])
output.to_csv("labels_final.csv", index=False, encoding="utf-8-sig")

# Ozet tablo
print("=" * 70)
print("FINAL TOPIC -> SUBTOPIC YAPISI")
print("=" * 70)

for topic in sorted(df["topic"].unique()):
    topic_count = (df["topic"] == topic).sum()
    print(f"\n  {topic} ({topic_count} makale)")
    subs = df[df["topic"] == topic].groupby("subtopic").size().sort_values(ascending=False)
    for sub, count in subs.items():
        print(f"      - {sub}: {count}")

print(f"\n{'=' * 70}")
print(f"TOPLAM: {len(df)} makale | {df['topic'].nunique()} topic | {df['subtopic'].nunique()} subtopic")
print(f"Kaydedildi: labels_final.csv")
