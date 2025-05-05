# Symptom Checker

An AI-based symptom checker that provides preliminary health insights based on user-input symptoms.  
It uses a custom dataset derived from MedlinePlus and an Augmented Generation (RAG) pipeline
built with LangChain, FAISS, HuggingFace embeddings, and Groq for low-latency, high-speed inference.

## 🔧 Technologies Used
- Python
- HuggingFace (SBERT)
- MedlinePlus (scraped dataset)
- LangChain
- FAISS
- Groq (ChatGroq, LLaMA3)

## Project Structure
symptom-checker/
├── data/ # Cleaned and structured medical dataset
├── notebooks/ # Jupyter notebooks for analysis and prototyping
├── src/ # Main source code (retriever, parser, utilities)
│ ├── parser/ # script for webscraping of dataset
│ ├── preprocessing/ #script for cleaning of scaraped dataset 
│ ├── retriever/ # FAISS, langChain, groq based query pipeline
│ └── utils/ # Utility scripts and configurations
├── outputs/ # Sample responses
├── README.md # Project overview
├── LICENSE # MIT License
└── requirements.txt # Python dependencies

## Status
Work in progress, core pipeline under development and multilingual adaptation ongoing.
