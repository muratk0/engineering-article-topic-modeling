# 🏭 Engineering Article Topic Modeling & Classification

Automated topic modeling, taxonomy creation, and file classification system for **21,273+ mechanical engineering articles** using NLP and Machine Learning.

---

## 📌 Project Overview / Proje Özeti

### 🇬🇧 English
This project automatically categorizes over 21,000 unlabelled Markdown articles into a structured 2-level taxonomy (**Topic ➔ Subtopic**). It employs two distinct Unsupervised Machine Learning approaches to compare performance:
1. **Baseline Model (TF-IDF):** Vectorizes text based on keyword frequencies. Excellent at isolating specific machine types (e.g., Waterjets, Lasers).
2. **Advanced Model (Semantic Embeddings):** Uses `sentence-transformers` to capture the true contextual meaning of articles. **(Chosen as Final Deliverable)** as it correctly distinguishes between technical tutorials and corporate/economic news.

### 🇹🇷 Türkçe
Bu proje, etiketlenmemiş 21.000'den fazla makine mühendisliği makalesini Doğal Dil İşleme (NLP) kullanarak (**Topic ➔ Subtopic**) hiyerarşisinde otomatik olarak sınıflandırır. İki farklı yöntem kullanılmıştır:
1. **Temel Model (TF-IDF):** Kelime sıklığına göre çalışır. Belirli makine isimlerini ayırmada iyidir.
2. **Gelişmiş Model (Semantic Embeddings):** Makalelerin anlamsal bütünlüğünü kavramak için `sentence-transformers` kullanır. Şirket haberleri ile teknik makaleleri birbirinden mükemmel şekilde ayırdığı için **Nihai (Final) Model** olarak seçilmiştir.

---

## ⚙️ Methodology & Technical Architecture / Yöntem

### 1. TF-IDF + K-Means (Baseline Pipeline)
- Converted raw text into numerical vectors using `TfidfVectorizer`.
- Evaluated optimal clusters via Silhouette/Elbow, identifying **K=15**.
- Grouped into 7 Main Topics and 15 Subtopics. Very strict on technical keywords but lacks contextual understanding for business news.

### 2. Sentence-Transformers + K-Means (Final Embedding Pipeline)
- Utilized the `all-MiniLM-L6-v2` transformer model to convert articles into 384-dimensional dense semantic vectors.
- Evaluated optimal clusters via Silhouette/Elbow, identifying a strong peak at **K=10**.
- Grouped into **8 Main Topics and 10 Subtopics**. Successfully mapped semantic intent, separating regional manufacturing news from raw material discussions.

---

## 📊 Final Taxonomy (Embedding K=10) / Nihai Konu Hiyerarşisi

```
├── 1. Industry & Business
│   ├── Corporate & Regional Manufacturing News
│   ├── Fabrication Shop Stories & Profiles
│   └── Trade Shows & Exhibitions (EuroBLECH/Fabtech)
├── 2. Cutting Technologies
│   └── Laser & Precision Cutting
├── 3. Forming & Machinery
│   └── Hydraulic & Mechanical Presses
├── 4. Forming & Bending
│   └── Press Brake Tooling & Sheet Bending
├── 5. Welding
│   └── Welding Processes & Automation
├── 6. Technology & Software
│   └── Software & Smart Manufacturing (CAD-Data)
├── 7. Market & Economy
│   └── Global Market Trends & Steel Demand
└── 8. Materials & Processing
    └── Sheet Metal Forming & Raw Materials
```

---

## 📂 Repository Structure / Klasör Yapısı

```
├── data/                             # Raw articles (Excluded from Git)
├── organized_embedding_data/         # Final physically organized folders (Excluded from Git)
│
├── 📁 experiment_embedding/          # ➔ FINAL EMBEDDING PIPELINE
│   ├── cluster_embedding.py          # Master embedding generation & K=10 clustering script
│   ├── organize_embedding_files.py   # Script to physically sort files into folders
│   ├── optimal_k_embedding.png       # Evaluation graph proving K=10 is optimal
│   ├── labels_embedding_final.csv    # FINAL DELIVERABLE: The exact taxonomy mapping
│   └── cross_check.py                # QA script comparing TF-IDF vs Embedding results
│
├── cluster_tfidf.py                  # ➔ BASELINE TF-IDF PIPELINE (Legacy master script)
├── find_optimal_k.py                 # Graph evaluation for TF-IDF (K=15)
├── optimal_k.png                     # Graph output for TF-IDF
├── labels_final.csv                  # Legacy TF-IDF taxonomy mapping
├── organize_files.py                 # Legacy file organizer
└── README.md                         # Project documentation
```

---

## 🚀 How to Run / Nasıl Çalıştırılır?

### Running the Final Embedding Pipeline
```bash
# 1. Install required AI and ML libraries
pip install scikit-learn pandas matplotlib sentence-transformers torch

# 2. Execute the master embedding script (Takes ~10 mins on CPU)
# (Generates embeddings, clusters with K=10, and outputs labels_embedding_final.csv)
cd experiment_embedding
python cluster_embedding.py

# 3. Organize the physical .md files into Topic/Subtopic folders
python organize_embedding_files.py
```

### Running the Baseline TF-IDF Pipeline
```bash
# 1. Execute the master TF-IDF script
python cluster_tfidf.py
```

---

## 📈 Evaluation Results / Evaluasyon
- **Total Articles Processed:** 21,273
- **Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2`
- **Vector Dimensions:** 384
- **Final Selected K:** 10 (Chosen via Silhouette Score analysis)
