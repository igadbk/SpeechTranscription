import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_video_uri():
    # Ścieżka do pliku JSON z danymi uwierzytelniającymi
    credentials_file = 'lala.json'

    # Utwórz zasięg uwierzytelniania
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    # Uzyskaj poświadczenia uwierzytelniania
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)

    # Utwórz klienta sesji
    client = gspread.authorize(credentials)

    # Otwórz arkusz Google Sheets
    spreadsheet = client.open('lala')  # Zastąp 'Nazwa_arkusza' nazwą swojego arkusza

    # Wybierz arkusz
    worksheet = spreadsheet.sheet1

    # Odczytaj wartość z komórki A1
    cell_value = worksheet.acell('A1').value

    # Zwróć odczytaną wartość jako video_uri
    return cell_value

# Użyj funkcji get_video_uri do uzyskania video_uri
video_uri = get_video_uri()

video = video_uri.split('/')[-2]

video1 = f"gs://speech_ig/{video}.mp4"

# Wyświetl odczytany video_uri
print(video1)

