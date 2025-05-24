import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load .env file (optional if you've exported the key directly)
load_dotenv()

# Get the API key
api_key = os.getenv("API_KEY")

# Check if key is present
if not api_key:
    raise ValueError("API_KEY not found in environment variables.")

# Configure the API
genai.configure(api_key=api_key)

# Try using a known model
try:
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content("Say hello in a creative way.")
    print("API key works!")
    print("Response:", response.text)
except Exception as e:
    print(" API key test failed.")
    print("Error:", e)
