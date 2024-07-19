from pytube import YouTube

# Function to download YouTube video
def download_youtube_video(url, save_path):
    try:
        # Create a YouTube object
        yt = YouTube(url)
        
        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()
        
        # Download the video
        stream.download(save_path)
        
        print(f"Video downloaded successfully and saved to {save_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# URL of the YouTube video
video_url = "https://youtu.be/bKpA6Nxiz2c"  # Replace with the actual URL

# Path to save the downloaded video
save_path = r"C:\Users\Herbert\Downloads"  # Replace with the actual path

# Call the download function
download_youtube_video(video_url, save_path)

