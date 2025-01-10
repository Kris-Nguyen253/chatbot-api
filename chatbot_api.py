from flask import Flask, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Hàm kết nối Google Sheets
def connect_google_sheets(spreadsheet_id):
    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ])
        client = gspread.authorize(creds)
        spreadsheet = client.open_by_key(spreadsheet_id)
        print(f"Connected to Google Sheet with ID: {spreadsheet_id}")  # Debug log
        sheet = spreadsheet.get_worksheet(0)
        return sheet
    except Exception as e:
        print(f"Error connecting to Google Sheets: {e}")  # Debug log
        raise e

# Hàm đọc dữ liệu từ Google Sheets
def get_keywords_responses(sheet):
    try:
        data = sheet.get_all_records()
        responses = {row["Keyword"]: row["Response"] for row in data}
        print("Dữ liệu từ Google Sheets:", responses)  # Debug log
        return responses
    except Exception as e:
        print(f"Error reading data from Google Sheets: {e}")  # Debug log
        raise e

# Endpoint API để xử lý tin nhắn
@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Nhận dữ liệu từ client
        request_data = request.json
        print(f"Request data: {request_data}")  # Debug log
        user_message = request_data.get("message", "").strip()
        print(f"User message: {user_message}")  # Debug log

        # Kết nối Google Sheets
        spreadsheet_id = "1HCHNotMHzfo2PleqnUWlJTB1QJ7SUs8dJiy9jU0FWXE"
        sheet = connect_google_sheets(spreadsheet_id)

        # Đọc dữ liệu từ Google Sheets
        responses = get_keywords_responses(sheet)

        # Tìm phản hồi tương ứng
        bot_response = responses.get(user_message, "Xin lỗi, tôi không hiểu câu hỏi của bạn.")
        print(f"Bot response: {bot_response}")  # Debug log
        return jsonify({"response": bot_response})
    except Exception as e:
        print(f"Lỗi khi xử lý tin nhắn: {e}")  # Debug log
        return jsonify({"response": "Đã xảy ra lỗi, vui lòng thử lại sau."})

if __name__ == "__main__":
    app.run(port=5000)
