# **Documentation for Video Transcription Script**

## **Requirements**

* Python 3.7 or newer.
* Install required libraries using pip install --upgrade google-cloud-videointelligence gspread oauth2client.
* A Google Cloud account with a created project.
* The Cloud Video Intelligence API service is enabled in the Google Cloud Console for the given project.
* A created JSON key file for the service account.
* The path to the JSON key file of the service account, set as the value for GOOGLE_APPLICATION_CREDENTIALS.
* A video file to be transcribed, uploaded to Google Cloud Storage.
* A Google Spreadsheet shared with the service account email.

## **Usage**

* Configure the environment variable GOOGLE_APPLICATION_CREDENTIALS to point to the JSON key file for the Google Cloud service account. The key file should be generated in Google Cloud Console and downloaded to your local drive.
* Replace the placeholders 'path_to_your_service_account_file.json' and 'Your Spreadsheet Name' with your actual values.
* Run the script. The script will process the video and the transcription result will be saved to the specified Google Spreadsheet.

## **Video URI**

* The input_uri in the script refers to the URI of the video file stored in Google Cloud Storage that you want to transcribe. It's a string that follows this format: gs://BUCKET_NAME/FILE_NAME, where BUCKET_NAME is the name of your Google Cloud Storage bucket and FILE_NAME is the name of your video file.
* Please make sure that the video file is uploaded to Google Cloud Storage and the service account has appropriate permissions to access the file. If your video is not in a Google Cloud Storage bucket, you will need to upload it there first before running this script.
* If you encounter issues, make sure:
> * The video file is present at the indicated location on Google Cloud Storage, i.e., the input_uri is correctly pointing to the video file you intend to transcribe.
> * The service account has the necessary permissions to access the video file in the bucket. You can set the permissions in the Google Cloud Console.
> * The video file is in a format supported by the Cloud Video Intelligence API (for instance, MP4, AVI, FLV, MOV, etc.).

## **Troubleshooting**

* Authorization issue: Ensure that the path to the JSON key file is correct and the file exists. Make sure the Cloud Video Intelligence API service is enabled for your project in Google Cloud Console.
* Transcription issue: Make sure the video file exists at the indicated location on Google Cloud Storage and that the service account has access to it.
* Issue with writing to Google Spreadsheet: Ensure that the service account's email has been added to the shared users in Google Spreadsheet.
* Library-related errors: Ensure you've installed all the required libraries. If you're using a virtual environment, make sure the libraries are installed in the correct environment.