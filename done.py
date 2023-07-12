import os
import gspread
from google.cloud import videointelligence
from oauth2client.service_account import ServiceAccountCredentials
from uri import done

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'

# Set up the scope
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# Instantiate the client
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# Open the Google Spreadsheet by its name (Make sure you have shared it with the client email)
sheet = client.open('SPREADSHEET_NAME').sheet1

def update_transcription_to_sheet(transcription):
    # Update cell B1 with the actual transcription result
    sheet.update('B1', transcription)

def videoinspector(video_urii, transcribe=True):
    # Set up the video intelligence client
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.Feature.SPEECH_TRANSCRIPTION]

    # Define the configurations as raw dictionaries
    config = {"language_code": "en-US", "enable_automatic_punctuation": True}
    video_context = {"speech_transcription_config": config}

    # Submit the video transcription request
    operation = video_client.annotate_video(
        request={
            "features": features,
            "input_uri": video_urii,
            "video_context": video_context,
        }
    )

    if transcribe:
        result = operation.result()

        annotation_results = result.annotation_results[0]
        transcription = ""
        for speech_transcription in annotation_results.speech_transcriptions:
            for alternative in speech_transcription.alternatives:
                transcription += "Transcription: {}\n".format(alternative.transcript)
                transcription += "Confidence: {}\n\n".format(alternative.confidence)

        update_transcription_to_sheet(transcription)

# Display the "Processing. Please wait..." message in cell B1
sheet.update('B1', "Processing. Please wait...")

# Create the video URI
video_urii = done

# Call the videoinspector function
videoinspector(video_urii, transcribe=True)


















