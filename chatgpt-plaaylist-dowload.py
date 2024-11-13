import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import yt_dlp
import os
from ttkbootstrap import Style

# Initialize TTK Bootstrap Style
style = Style(theme='cosmo')  # You can change the theme as desired

# Create the main window
root = style.master
root.title("YouTube Video & Playlist Downloader")
root.geometry("800x400")

# Functions


def download_playlist(url, selected_format_id, save_path):
    """Downloads all videos in the playlist in the selected format."""
    ydl_opts = {
        'format': selected_format_id,  # Download the format selected by the user
        'outtmpl': f"{save_path}/%(title)s.%(ext)s",
        'noprogress': False,  # Show download progress
        'retries': 10,  # Increase retries
        'timeout': 30,  # Set timeout to 30 seconds
        'fragment_retries': 10,  # Retry fragmented downloads
        'continuedl': True,  # Enable resumable downloads
        # Disable SSL certificate verification (optional)
        'nocheckcertificate': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "All videos downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download playlist: {str(e)}")


def start_download():
    """Start downloading the selected playlist."""
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Warning", "Please enter a playlist URL.")
        return

    save_path = filedialog.askdirectory()
    if not save_path:
        return

    selected_format_id = format_entry.get().strip()
    if not selected_format_id:
        messagebox.showwarning("Warning", "Please select a download format.")
        return

    # Start download
    download_playlist(url, selected_format_id, save_path)


# UI Layout
frame = ttk.Frame(root)
frame.pack(pady=10)

url_label = ttk.Label(frame, text="YouTube Playlist URL:")
url_label.grid(row=0, column=0, padx=5)

url_entry = ttk.Entry(frame, width=50)
url_entry.grid(row=0, column=1, padx=5)

format_label = ttk.Label(
    root, text="Select Download Format (e.g., best, 720p):")
format_label.pack(pady=10)

format_entry = ttk.Entry(root, width=50)
format_entry.pack(pady=5)

download_button = ttk.Button(
    root, text="Download Playlist", command=start_download)
download_button.pack(pady=10)

# Start the application
root.mainloop()
