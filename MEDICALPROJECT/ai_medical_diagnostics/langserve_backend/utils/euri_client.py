import requests
import json

API_KEY = "euri-a95ddaa9c5e3d3989c07a3f3ce3f8918966c70401e8370a29d1dde239b561a5f"
BASE_URL = "https://api.euron.one/api/v1/euri"

def euri_chat_completion(messages, model="gpt-4.1-nano", temperature=0.7, max_tokens=1000):
    url = f"{BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    
    try:
        print(f"Making request to: {url}")
        print(f"Payload: {json.dumps(payload, indent=2)}")
        
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        
        print(f"Response status code: {response.status_code}")
        
        # Check if request was successful
        if response.status_code != 200:
            print(f"API Error - Status: {response.status_code}")
            print(f"Response text: {response.text}")
            raise Exception(f"API request failed with status {response.status_code}: {response.text}")
        
        # Parse JSON response
        response_data = response.json()
        print(f"Response data: {json.dumps(response_data, indent=2)}")
        
        # Check if response has expected structure
        if "choices" not in response_data:
            print(f"Error: 'choices' key not found. Available keys: {list(response_data.keys())}")
            # Check for error message in response
            if "error" in response_data:
                raise Exception(f"API returned error: {response_data['error']}")
            else:
                raise KeyError(f"Unexpected response format. Expected 'choices' key, got: {list(response_data.keys())}")
        
        if not response_data["choices"]:
            raise ValueError("No choices returned in API response")
        
        if "message" not in response_data["choices"][0]:
            raise KeyError("No 'message' key in first choice")
        
        if "content" not in response_data["choices"][0]["message"]:
            raise KeyError("No 'content' key in message")
        
        return response_data["choices"][0]["message"]["content"]
        
    except requests.exceptions.Timeout:
        print("Request timed out")
        raise Exception("API request timed out after 30 seconds")
    except requests.exceptions.ConnectionError:
        print("Connection error")
        raise Exception("Failed to connect to API endpoint")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        raise Exception(f"Request failed: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        print(f"Response text: {response.text}")
        raise Exception(f"Failed to parse API response as JSON: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise


def test_api_connection():
    """Test function to check if the API is working"""
    test_messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say hello"}
    ]
    
    try:
        result = euri_chat_completion(test_messages)
        print(f"API test successful: {result}")
        return True
    except Exception as e:
        print(f"API test failed: {e}")
        return False


def simple_medical_response(symptom_description):
    """Fallback function when API is unavailable"""
    return f"""Based on the symptoms you've described: "{symptom_description}"

I'm currently unable to provide a detailed analysis due to technical issues. However, here are some general recommendations:

1. **Seek Professional Medical Advice**: For any health concerns, please consult with a qualified healthcare provider who can properly examine you and provide accurate diagnosis.

2. **Emergency Situations**: If you're experiencing severe symptoms, difficulty breathing, chest pain, or other emergency signs, please seek immediate medical attention.

3. **Document Your Symptoms**: Keep track of when symptoms started, their severity, and any patterns you notice.

**IMPORTANT DISCLAIMER**: This tool is for educational purposes only and should not replace professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider for medical concerns."""


if __name__ == "__main__":
    # Test the API connection
    print("Testing API connection...")
    test_api_connection()