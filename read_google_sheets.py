import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Hàm kết nối tới Google Sheets
def connect_google_sheets(spreadsheet_id):
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ])
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_key(spreadsheet_id)  # Mở Google Sheets bằng ID
    sheet = spreadsheet.get_worksheet(0)  # Lấy worksheet đầu tiên
    return sheet

# Hàm đọc dữ liệu từ Google Sheets
def get_keywords_responses(sheet):
    try:
        data = sheet.get_all_records()
        if not data:
            print("Google Sheet trống hoặc không có dữ liệu!")
            return {}
        print("Dữ liệu đã lấy thành công:")
        for row in data:
            print(row)
        return {row["Keyword"]: row["Response"] for row in data}
    except Exception as e:
        print(f"Lỗi khi đọc dữ liệu từ Google Sheets: {e}")
        return {}

# Chạy thử
if __name__ == "__main__":
    spreadsheet_id = "1HCHNotMHzfo2PleqnUWlJTB1QJ7SUs8dJiy9jU0FWXE"  # ID Google Sheet
    sheet = connect_google_sheets(spreadsheet_id)
    if sheet:
        responses = get_keywords_responses(sheet)
        print("Dữ liệu đã được tải vào dictionary:")
        print(responses)
    else:
        print("Không thể kết nối tới Google Sheets.")
