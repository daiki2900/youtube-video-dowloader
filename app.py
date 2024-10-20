import os
import yt_dlp
import ttkbootstrap as ttk
from tkinter import filedialog, StringVar, messagebox

# Function to update the progress bar


def progress_hook(d):
    if d['status'] == 'downloading':
        downloaded_bytes = d.get('downloaded_bytes', 0)
        total_bytes = d.get('total_bytes', 1)  # avoid division by zero
        progress_percent = (downloaded_bytes / total_bytes) * 100
        progress_var.set(progress_percent)
        app.update_idletasks()

# Function to download video in the highest resolution with progress tracking


def download_video():
    url = url_var.get()
    download_path = path_var.get()

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return
    if not download_path:
        messagebox.showerror("Error", "Please select a download location")
        return

    # Reset progress bar
    progress_var.set(0)

    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Download best video and audio available
            # Save with video title
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'progress_hooks': [progress_hook]  # Hook for progress update
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Download completed!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Function to select download path


def select_download_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        path_var.set(folder_selected)


# Initialize main window with a dark theme
app = ttk.Window(themename="litera")  # Changed to 'darkly' for dark theme
app.title("YouTube Video Downloader")
app.geometry("400x300")

# Set custom fonts
title_font = ("Arial", 16, "bold")
label_font = ("Arial", 12)
entry_font = ("Arial", 10)
button_font = ("Arial", 12, "bold")

# Define a style for buttons
style = ttk.Style()
style.configure("TButton", font=button_font)  # Apply font to buttons

# URL input field
url_var = StringVar()
url_label = ttk.Label(app, text="YouTube URL:", font=label_font)
url_label.pack(pady=10)
url_entry = ttk.Entry(app, textvariable=url_var, font=entry_font, width=50)
url_entry.pack(pady=5)

# Download path selector
path_var = StringVar()
path_label = ttk.Label(app, text="Download Path:", font=label_font)
path_label.pack(pady=10)
path_entry = ttk.Entry(app, textvariable=path_var, font=entry_font, width=50)
path_entry.pack(pady=5)

path_button = ttk.Button(app, text="Browse", command=select_download_path,
                         bootstyle="info")  # Using the new button style
path_button.pack(pady=5)

# Progress bar
progress_var = ttk.DoubleVar(value=0)
progress_bar = ttk.Progressbar(
    app, variable=progress_var, maximum=100, bootstyle="info-striped")
progress_bar.pack(pady=10, padx=20, fill="x")

# Download button
download_button = ttk.Button(app, text="Download", bootstyle="success",
                             command=download_video)  # Using the new button style
download_button.pack(pady=20)

# Run the app
app.mainloop()
