import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key từ file .env
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)
