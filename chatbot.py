from dotenv import load_dotenv
import openai
import os

# Tải API key từ file .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot_response(user_input):
    try:
        # Sử dụng model gpt-3.5-turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("Chatbot đã sẵn sàng! Gõ 'exit' để thoát.")
    while True:
        user_input = input("Bạn: ")
        if user_input.lower() == "exit":
            print("Tạm biệt!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
