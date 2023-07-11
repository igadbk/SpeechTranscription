import os
import gspread
from google.cloud import videointelligence
from oauth2client.service_account import ServiceAccountCredentials
from uri import done

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'lala.json'

# Set up the scope
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# Instantiate the client
creds = ServiceAccountCredentials.from_json_keyfile_name('lala.json', scope)
client = gspread.authorize(creds)

# Open the Google Spreadsheet by its name (Make sure you have shared it with the client email)
sheet = client.open('lala').sheet1

def update_transcription_to_sheet(transcription):
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
        print("Processing. Please wait...")
        result = operation.result()

        annotation_results = result.annotation_results[0]
        transcription = ""
        for speech_transcription in annotation_results.speech_transcriptions:
            for alternative in speech_transcription.alternatives:
                transcription += "Transcription: {}\n".format(alternative.transcript)
                transcription += "Confidence: {}\n\n".format(alternative.confidence)

        update_transcription_to_sheet(transcription)
    else:
        print("Processing. Please wait... (Transcription disabled)")


# Get the URL from cell A1
#cell = sheet.cell(1, 1)
#video_url = video_uri

# Extract the video ID from the URL
#video_id = video_url.split('/')[-2]

# Create the video URI
video_urii = done

# Call the videoinspector function
videoinspector(video_urii, transcribe=True)
