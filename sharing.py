
import os
import googleapiclient.discovery
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload

# Manually set the tokens
access_token = "Enter your access Token"
refresh_token = "Enter your refresh token"
token_uri = 'https://oauth2.googleapis.com/token' 
client_id = 'Enter your client ID'   
client_secret = 'Enter your client secret'  

scopes = ["https://www.googleapis.com/auth/youtube.upload"]

def upload_video(youtube, file_path, title, description, privacy_status):
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
            },
            "status": {
                "privacyStatus": privacy_status,
            },
        },
        media_body=MediaFileUpload(file_path)
    )
    response = request.execute()
    return response

def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"

    # Manually create credentials
    credentials = Credentials(
        token=access_token,
        refresh_token=refresh_token,
        token_uri=token_uri,
        client_id=client_id,
        client_secret=client_secret,
        scopes=scopes
    )

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    video_file_path = "Enter the path to your video file"  
    video_title = "Video test"
    video_description = "this is a fisr description video"
    privacy_status = "public"  # You can change this to "public" if you want the video to be public

    response = upload_video(youtube, video_file_path, video_title, video_description, privacy_status)

    print("Video uploaded successfully!")
    
    # Print the entire response
    for key, value in response.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
