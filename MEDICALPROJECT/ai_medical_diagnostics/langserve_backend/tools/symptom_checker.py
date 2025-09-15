from langchain.tools import tool

@tool
def check_symptom(symptom):
    """this tool will analyze the input symptom text and return the relevent medical category"""
    symptom= symptom.lower()
    if "fever" in symptom or "cough" in symptom or "sore throat" in symptom:
        return "Respiratory"
    elif "headache" in symptom or "dizziness" in symptom:
        return "Neurological"
    elif "stomach" in symptom or "nausea" in symptom or "diarrhea" in symptom:
        return "Gastrointestinal"
    elif "chest pain" in symptom or "shortness of breath" in symptom:
        return "Cardiovascular"
    elif "rash" in symptom or "itching" in symptom:
        return "Dermatological"
    else:
        return "General"
    

