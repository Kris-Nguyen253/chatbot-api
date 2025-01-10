import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Hàm kết nối tới Google Sheets bằng ID
def connect_google_sheets(spreadsheet_id):
    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ])
        client = gspread.authorize(creds)
        sheet = client.open_by_key(spreadsheet_id).sheet1
        print(f"Đã kết nối tới Google Sheet với ID: {spreadsheet_id}")
        return sheet
    except gspread.SpreadsheetNotFound:
        print("Lỗi: Không tìm thấy Google Sheets. Kiểm tra lại ID.")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
    return None

# Hàm lấy dữ liệu từ Google Sheets
def get_sheet_data(sheet):
    try:
        data = sheet.get_all_records()
        if not data:
            print("Google Sheet trống hoặc không có dữ liệu!")
        else:
            print("Dữ liệu đã lấy thành công:")
            for row in data:
                print(row)
        return data
    except Exception as e:
        print(f"Lỗi khi lấy dữ liệu từ Google Sheets: {e}")
        return None

# Chạy thử chương trình
if __name__ == "__main__":
    # Thay ID Google Sheet của bạn tại đây
    spreadsheet_id = "1HCHNotMHzfo2PleqnUWlJTB1QJ7SUs8dJiy9jU0FWXE"
    
    # Kết nối tới Google Sheets
    sheet = connect_google_sheets(spreadsheet_id)
    
    # Nếu kết nối thành công, lấy dữ liệu
    if sheet:
        data = get_sheet_data(sheet)
        if data:
            print("Dữ liệu từ Google Sheets đã hiển thị ở trên.")
        else:
            print("Không có dữ liệu để hiển thị.")
    else:
        print("Không thể kết nối tới Google Sheets.")
