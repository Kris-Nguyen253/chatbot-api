from dotenv import load_dotenv
import openai
import os

# Tải API key từ file .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    # Kiểm tra API key
    response = openai.Engine.list()
    print("API key hoạt động tốt!")
except Exception as e:
    print(f"Lỗi: {str(e)}")


