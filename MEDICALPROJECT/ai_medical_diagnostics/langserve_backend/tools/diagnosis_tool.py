from langchain.tools import tool
from utils.euri_client import euri_chat_completion


@tool
def ai_diagnos(symptom_description):
    """
    Analyzes patient symptoms and provides potential medical diagnoses with treatment recommendations.
    
    Args:
        symptom_description: Description of the patient's symptoms
        
    Returns:
        AI-generated diagnosis with potential cures and recommendations for patient relief
    """
    messages = [
        {"role": "system", "content": "You are a helpful medical assistant."},
        {"role": "user", "content": f"Given the following symptoms, provide a possible diagnosis: {symptom_description} , Also provide cure and what would make patient feel better"}
    ]
    response = euri_chat_completion(messages)
    return response