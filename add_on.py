from pytube import YouTube
import pandas as pd
import os


def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        return True, f"Video downloaded successfully: {stream.title}"
    except Exception as e:
        return False, f"Error downloading video: {str(e)}"


def download_videos_from_excel(excel_file_path, output_directory):
    # Read Excel file
    try:
        df = pd.read_excel(excel_file_path)
    except Exception as e:
        print("Error reading Excel file:", e)
        return

    # Ensure output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterate over rows and download videos
    for index, row in df.iterrows():
        name = str(row['Name'])  # Assuming the column name containing names is 'Name'
        url = str(row['URL'])  # Assuming the column name containing URLs is 'URL'

        # Parse filename from URL
        filename = name + ".mp4"

        # Download the video
        try:
            success, message = download_video(url)
            if success:
                os.rename(name + ".mp4", os.path.join(output_directory, filename))
                print(f"Downloaded: {filename}")
            else:
                print(f"Failed to download: {filename}. Reason: {message}")
        except Exception as e:
            print(f"Error downloading {filename}: {e}")


excel_file_path1 = 'songs.xlsx'
output_directory1 = 'Songs'
download_videos_from_excel(excel_file_path1, output_directory1)
