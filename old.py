import os
import gspread
from google.cloud import videointelligence
from oauth2client.service_account import ServiceAccountCredentials

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path_to_your_service_account_file.json'

# Set up the scope
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# Add your service account file
creds = ServiceAccountCredentials.from_json_keyfile_name('sheetsdemo.json', scope)

# Instantiate the client
client = gspread.authorize(creds)

# Open the Google Spreadsheet by its name (Make sure you have shared it with the client email)
sheet = client.open('Your Spreadsheet Name').sheet1

video_client = videointelligence.VideoIntelligenceServiceClient()
features = [videointelligence.Feature.SPEECH_TRANSCRIPTION]

# Define the configurations as raw dictionaries
config = {"language_code": "en-US", "enable_automatic_punctuation": True}
video_context = {"speech_transcription_config": config}

operation = video_client.annotate_video(
    request={
        "features": features,
        "input_uri": "gs://BUCKET_NAME/FILE_NAME",
        "video_context": video_context,
    }
)
print("\nProcessing. Please wait...")

result = operation.result()

annotation_results = result.annotation_results[0]
for speech_transcription in annotation_results.speech_transcriptions:
    for alternative in speech_transcription.alternatives:
        print("Alternative level info:")
        print("Transcription: {}".format(alternative.transcript))
        print("Confidence: {}\n".format(alternative.confidence))

        # Append the data to the spreadsheet
        sheet.append_row(["Transcription: {}".format(alternative.transcript), "Confidence: {}\n".format(alternative.confidence)])