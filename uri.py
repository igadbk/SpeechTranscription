import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_video_uri():
    # Path to the JSON file with authentication data
    credentials_file = 'lala.json'

    # Create authentication scope
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    # Obtain authentication credentials
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)

    # Create a client session
    client = gspread.authorize(credentials)

    # Open the Google Sheets spreadsheet
    spreadsheet = client.open('lala')  # Replace 'Spreadsheet_Name' with the name of your spreadsheet

    # Select the worksheet
    worksheet = spreadsheet.sheet1

    # Read the value from cell A1
    cell_value = worksheet.acell('A1').value

    # Return the read value as video_uri
    return cell_value

# Use the get_video_uri function to obtain video_uri
video_uri = get_video_uri()

video = video_uri.split('/')[-1]

video1 = f"gs://speech_ig/{video}"

done = video1

# Display the obtained video_uri
print(done)


