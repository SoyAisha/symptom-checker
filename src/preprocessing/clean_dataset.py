import pandas as pd 

# Caricare i dataset
df_HF = pd.read_csv("/Users/letizi4v/Desktop/nuovi df/Formatted_Dataset.csv")
df_MP = pd.read_csv("/Users/letizi4v/Desktop/nuovi df/mediline.csv")

# Normalizzare i nomi delle colonne
df_HF.columns = df_HF.columns.str.strip().str.lower().str.replace(" ", "_")
df_MP.columns = df_MP.columns.str.strip().str.lower().str.replace(" ", "_")

# Rinominare per uniformità
df_HF.rename(columns={"illness_name": "illness", "symptoms": "symptoms"}, inplace=True)
df_MP.rename(columns={"illness": "illness", "symptoms": "symptoms"}, inplace=True)

# Funzione per convertire stringhe in liste senza usare ast
def clean_symptom_string(symptom_str):
    if isinstance(symptom_str, str):
        # Rimuovere caratteri non necessari e splittare correttamente
        symptom_str = symptom_str.replace("[", "").replace("]", "").replace("'", "").replace('"', "")
        return [s.strip().lower() for s in symptom_str.split(",") if s.strip()]
    return []

# Applicare la conversione nel dataset di MedlinePlus (df_MP)
df_MP["symptoms"] = df_MP["symptoms"].apply(clean_symptom_string)

# Applicare la conversione nel dataset di Hugging Face (df_HF)
df_HF["symptoms"] = df_HF["symptoms"].apply(lambda x: [s.strip().lower() for s in x.split(",")] if isinstance(x, str) else [])

# Verifica delle conversioni
print("\nEsempio di sintomi convertiti in df_MP:")
print(df_MP["symptoms"].head())

print("\nEsempio di sintomi convertiti in df_HF:")
print(df_HF["symptoms"].head())

def count_duplicates(symptom_list):
    seen = set()
    duplicates = 0
    for symptom in symptom_list:
        if symptom in seen:
            duplicates += 1
        else:
            seen.add(symptom)
    return duplicates

# Applicare la funzione per contare i duplicati nei due dataset
df_HF["duplicate_count"] = df_HF["symptoms"].apply(count_duplicates)
df_MP["duplicate_count"] = df_MP["symptoms"].apply(count_duplicates)

# Contare il totale dei duplicati nei dataset
total_duplicates_HF = df_HF["duplicate_count"].sum()
total_duplicates_MP = df_MP["duplicate_count"].sum()

# Mostrare il numero di duplicati
print(f"Numero totale di sintomi duplicati in df_HF: {total_duplicates_HF}")
print(f"Numero totale di sintomi duplicati in df_MP: {total_duplicates_MP}")


df_HF["symptoms"] = df_HF["symptoms"].apply(lambda x: list(dict.fromkeys(x)))
df_HF["duplicate_count"] = df_HF["symptoms"].apply(lambda x: len(x) - len(set(x)))
print("Numero totale di sintomi duplicati dopo la pulizia:", df_HF["duplicate_count"].sum())


df_HF[df_HF.duplicated(subset=["illness"], keep=False)]
df_HF_cleaned = df_HF.groupby("illness", as_index=False).agg({"symptoms": lambda x: sorted(set(sum(x, [])))})

# Mostrare il numero di malattie dopo la pulizia
print(f"Numero totale di malattie uniche dopo la pulizia: {df_HF_cleaned['illness'].nunique()}")

# Verificare che i duplicati siano stati eliminati
print(f"Malattie duplicate dopo la pulizia: {df_HF_cleaned.duplicated(subset=['illness']).sum()}") 


df_HF_cleaned.to_csv("/mnt/data/HUGFACE_cleaned.csv", index=False)
df_MP.to_csv("/mnt/data/mediline_cleaned.csv", index=False)
