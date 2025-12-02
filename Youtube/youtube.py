from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Video download successfully!")

    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter your Youtube URL: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")
    






# url = "https://www.youtube.com/watch?v=_3q35ghBE3Y&list=RD_3q35ghBE3Y&start_radio=1"
# url2 = "https://www.youtube.com/watch?v=Eakt1tkxIXc&list=RD_3q35ghBE3Y&index=4"

# save_path = "C:/Users/ASUS/Videos/Youtube"

# download_video(url2, save_path)