from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
import sys

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        if not streams:
            print("No MP4 video streams available.")
            return

        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"Error: {e}")

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory()
    return folder

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <YouTube_URL>")
        sys.exit(1)

    video_url = sys.argv[1]
    save_dir = open_file_dialog()

    if not save_dir:
        print("Invalid save location.")
        sys.exit(1)

    print("Started download...")
    download_video(video_url, save_dir)

if __name__ == "__main__":
    main()
