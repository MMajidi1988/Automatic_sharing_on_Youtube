# Automatic_sharing_on_Youtube
# YouTube Video Uploader README

This Python script provides a straightforward way to upload videos to YouTube using the YouTube Data API v3. It's designed to automate the video upload process by using OAuth 2.0 for authentication.

## Features

- Upload videos to YouTube.
- Set video details like title, description, and privacy status.
- Authenticate using OAuth 2.0 credentials.

## Requirements

- Python 3.x
- `google-api-python-client` and `google-auth` libraries.

  Install these libraries using pip:
  ```
  pip install --upgrade google-api-python-client google-auth
  ```

## Setup

1. **Credentials**: Before using the script, you'll need to have your OAuth 2.0 credentials from Google Cloud Platform. These include `access_token`, `refresh_token`, `client_id`, and `client_secret`.

2. **Create a Project in Google Cloud Console**: 
   - Go to [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project.
   - Go to the "APIs & Services" -> "Credentials" section.
   - Set up your OAuth consent screen.
   - Create credentials (OAuth client ID).
   - Download the JSON file and extract the required credentials.

3. **Enable YouTube Data API**: 
   - In the Google Cloud Console, navigate to the "API & Services" dashboard.
   - Click “+ ENABLE APIS AND SERVICES”.
   - Search for "YouTube Data API v3" and enable it.

## Usage

1. **Edit the Script**: Replace the placeholders in the script with your actual OAuth credentials.

2. **Set Video Details**: Modify the `video_file_path`, `video_title`, `video_description`, and `privacy_status` in the `main` function to fit your requirements.

3. **Run the Script**: Execute the script in your Python environment.
   ```
   python youtube_video_uploader.py
   ```

4. **Check the Output**: After running the script, it will print the response from the YouTube API including the URL of the uploaded video.

## Security Note

Never share your OAuth credentials publicly. If you're planning to host this code on a public repository (like GitHub), make sure to remove or secure your credentials.

## Contributions

Feel free to fork this repository and contribute by submitting a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Disclaimer

This script is provided "as is", without warranty of any kind. Use at your own risk. 

**Happy Coding!** 🎥👩‍💻👨‍💻
