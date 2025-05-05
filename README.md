# Symptom Checker

An AI-based symptom checker that provides preliminary health insights based on user-input symptoms.  
It uses a custom dataset derived from MedlinePlus and a Retrieval-Augmented Generation (RAG) pipeline  
built with LangChain, FAISS, HuggingFace embeddings, and Groq for fast, low-latency inference.

---

## 🔧 Technologies Used
- Python
- LangChain
- FAISS
- HuggingFace (SBERT)
- Groq (ChatGroq, LLaMA3)
- MedlinePlus (scraped dataset)

## 🗂 Project Structure
symptom-checker/
├── data/ # Cleaned and structured medical dataset
├── notebooks/ # Jupyter notebooks for analysis and prototyping
├── src/ # Main source code (retriever, parser, utilities)
│ ├── retriever/ # FAISS, LangChain, Groq-based query pipeline
│ ├── parser/ # Data cleaning and structuring scripts
│ └── utils/ # Utility scripts and configurations
├── outputs/ # Sample responses or logs
├── README.md # Project overview
├── LICENSE # MIT License
└── requirements.txt # Python dependencies

## 📌 Status
Work in progress — core pipeline under development and multilingual adaptation ongoing.
