import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Load your API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ Error: API Key not found in .env file!")
else:
    print(f"✅ Found API Key: {api_key[:5]}...")

    # 2. Configure Google AI
    genai.configure(api_key=api_key)

    # 3. List all available models
    print("\n--- AVAILABLE MODELS FOR YOUR KEY ---")
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                # We only care about models that look like 'gemini'
                if 'gemini' in m.name:
                    print(f"- {m.name}")
    except Exception as e:
        print(f"❌ Error listing models: {e}")