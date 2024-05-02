import streamlit as st
from pytube import YouTube

# Streamlit app title
st.title('YouTube Video Downloader')

# Input for YouTube URL
video_url = st.text_input('Enter the YouTube video URL')


# Function to download video
def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        return True, f"Video downloaded successfully: {stream.title}"
    except Exception as e:
        return False, f"Error downloading video: {str(e)}"


# Button to download video
if st.button('Download Video'):
    success, message = download_video(video_url)
    if success:
        st.success(message)
    else:
        st.error(message)
