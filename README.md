# 📚 Engineering Article Topic Modeling & Classification

Automated topic modeling, taxonomy creation, and file classification system for **21,273+ mechanical engineering articles** using NLP and Machine Learning.

---

## 📌 Project Overview / Proje Özeti

### 🇬🇧 English
This project automatically categorizes over 21,000 unlabelled Markdown articles into a structured 2-level taxonomy (**Topic → Subtopic**). Using Natural Language Processing (NLP) and Unsupervised Machine Learning, articles are vectorized and clustered based on semantic word frequency, then organized into physical directories.

### 🇹🇷 Türkçe
Bu proje, etiketlenmemiş 21.000'den fazla makine mühendisliği makalesini Doğal Dil İşleme (NLP) ve Gözetimsiz Makine Öğrenmesi kullanarak 2 seviyeli bir hiyerarşide (**Topic → Subtopic**) otomatik olarak gruplar ve klasörler.

---

## 🛠️ Methodology & Technical Architecture / Yöntem

1. **Text Vectorization (TF-IDF):** 
   - Converted raw text into 500-dimensional numerical vectors using `TfidfVectorizer`.
   - Filtered out domain-agnostic stop words to highlight key technical terms (e.g., *welding, laser, hydraulic*).

2. **Optimal Cluster Evaluation (Elbow & Silhouette):**
   - Evaluated cluster count $K \in [5, 25]$ using **Inertia** (Elbow method) and **Silhouette Scores**.
   - Identified $K=15$ as the mathematical optimal point for intra-cluster cohesion and inter-cluster separation.

3. **Clustering & Taxonomy Mapping (K-Means):**
   - Partitioned dataset into 15 Subtopic clusters via **K-Means Clustering**.
   - Extracted top keyword features for each cluster center to assign human-readable Subtopic names.
   - Hierarchically grouped 15 Subtopics into **7 Main Industry Topics**.

4. **Automated Directory Structuring:**
   - Programmatically replicated the CSV taxonomy onto the file system (`organized_data/Topic/Subtopic/`).

---

## 📊 Taxonomy Structure / Konu Hiyerarşisi

```
├── 1. Cutting Technologies (2,917 articles)
│   ├── Laser Cutting
│   ├── Waterjet & Plasma Cutting
│   └── Surface Treatment & Plasma Tables
├── 2. Forming & Bending (4,926 articles)
│   ├── General Machinery & Tube Bending
│   ├── Press Brake & Hydraulic Systems
│   └── Bending Tooling & Die Design
├── 3. Industry & Business (9,226 articles)
│   ├── General Manufacturing & Production
│   ├── Company Profiles & Stories
│   ├── US Fabrication News (FMA/Fabtech)
│   ├── Trade Shows & Exhibitions
│   └── UK Manufacturing Sector
├── 4. Welding (1,360 articles)
│   └── Welding Processes & Robotics
├── 5. Materials (1,096 articles)
│   └── Steel & Raw Materials
├── 6. Market & Economy (1,454 articles)
│   └── Global Market Trends
└── 7. Design & Engineering (294 articles)
    └── CAD & 3D Modeling
```

---

## 📁 Repository Structure / Klasör Yapısı

```
├── data/                      # Raw articles (Excluded from Git)
├── organized_data/            # Programmatically organized articles (Excluded from Git)
├── cluster.py                 # Initial 10-cluster experiment script
├── find_optimal_k.py          # Optimal K evaluation script (Elbow & Silhouette)
├── optimal_k.png              # Generated evaluation graphs
├── cluster_v2.py              # Main 15-cluster K-Means execution script
├── create_final_labels.py     # Taxonomy mapping script (Generates labels_final.csv)
├── check_labels.py            # Quality assurance / sample validation script
├── organize_files.py          # File system directory organization script
├── labels_final.csv           # FINAL DELIVERABLE: Mapped article dataset
└── README.md                  # Project documentation
```

---

## 🚀 How to Run / Nasıl Çalıştırılır?

```bash
# 1. Install dependencies
pip install scikit-learn pandas matplotlib

# 2. Run optimal K evaluation (Generates optimal_k.png)
python find_optimal_k.py

# 3. Execute 15-cluster K-Means algorithm
python cluster_v2.py

# 4. Map clusters to 2-level taxonomy (Generates labels_final.csv)
python create_final_labels.py

# 5. Organize physical files into Topic/Subtopic directories
python organize_files.py
```

---

## 📈 Evaluation Results / Evaluasyon

- **Total Articles Processed:** 21,273
- **Total Words Analyzed:** ~20.6 Million
- **Unique Vocabulary:** 83,728
- **Final Taxonomy:** 7 Main Topics, 15 Subtopics
