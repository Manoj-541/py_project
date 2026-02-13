import pandas as pd

df = pd.read_csv("dataset.csv")

# -----------------------------
# Extract all unique symptoms
# -----------------------------
def get_all_symptoms():
    all_symptoms = set()

    for _, row in df.iterrows():
        symptoms = row["Symptoms"].split()
        for symptom in symptoms:
            all_symptoms.add(symptom)

    return sorted(list(all_symptoms))


# -----------------------------
# Disease Prediction Logic
# -----------------------------
def predict_disease(user_symptoms):

    best_match = None
    max_match_count = 0

    for _, row in df.iterrows():
        disease_symptoms = row["Symptoms"].split()

        match_count = len(set(user_symptoms) & set(disease_symptoms))

        if match_count > max_match_count:
            max_match_count = match_count
            best_match = row["Disease"]

    return best_match if best_match else "No matching disease found"
