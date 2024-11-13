import yt_dlp
import tkinter as tk
from tkinter import messagebox, filedialog
from ttkbootstrap import Style
from tkinter import ttk
import threading

# Global variable to store formats
available_formats = []


def fetch_formats(url, format_menu):
    """Fetches available formats for the given URL."""
    global available_formats

    ydl_opts = {
        'quiet': True,  # Suppress output
        'skip_download': True,  # We only want to fetch formats, not download
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            available_formats = info.get('formats', [])

            # Populate the format dropdown
            format_menu['values'] = [
                f"{fmt['format_id']} - {fmt['format_note']} - {fmt['ext']}"
                for fmt in available_formats if fmt.get('format_note')
            ]

            if available_formats:
                messagebox.showinfo(
                    "Formats Loaded", "Available formats have been loaded.")
            else:
                messagebox.showerror(
                    "Error", "No formats available for this video.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve formats: {str(e)}")


def download_video(url, progress, selected_format_id, save_path):
    """Downloads the video in the selected format."""
    def progress_hook(d):
        if d['status'] == 'downloading':
            if d.get('total_bytes'):
                percent = d['downloaded_bytes'] / d['total_bytes'] * 100
            elif d.get('total_bytes_estimate'):
                percent = d['downloaded_bytes'] / \
                    d['total_bytes_estimate'] * 100
            else:
                percent = 0
            progress['value'] = percent
            root.update_idletasks()
        elif d['status'] == 'finished':
            progress['value'] = 100
            messagebox.showinfo("Success", "Download Completed!")

    ydl_opts = {
        'format': selected_format_id,  # Download the format selected by the user
        'outtmpl': f"{save_path}/%(title)s.%(ext)s",
        'progress_hooks': [progress_hook],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {str(e)}")


def start_download(url, progress, selected_format, save_path):
    """Starts the download in a separate thread."""
    selected_format_id = selected_format.split(
        ' ')[0]  # Extract the format ID (first part of the string)
    download_thread = threading.Thread(target=download_video, args=(
        url, progress, selected_format_id, save_path))
    download_thread.start()


def choose_save_path():
    """Allows the user to choose the save location."""
    path = filedialog.askdirectory()
    if path:
        save_path_var.set(path)


def create_gui():
    global root
    # You can choose other themes like 'cosmo', 'flatly', etc.
    style = Style('litera')
    root = style.master
    root.title("YouTube Video Downloader")
    root.geometry('600x400')
    root.resizable(False, False)

    # Frame for URL entry
    url_frame = ttk.Frame(root, padding=10)
    url_frame.pack(fill='x')

    url_label = ttk.Label(url_frame, text="YouTube Video URL:")
    url_label.pack(side='left', padx=(0, 10))

    url_entry = ttk.Entry(url_frame, width=50)
    url_entry.pack(side='left', fill='x', expand=True)

    # Fetch Formats Button
    fetch_button = ttk.Button(root, text="Fetch Formats", command=lambda: fetch_formats(
        url_entry.get(), format_menu))
    fetch_button.pack(pady=10)

    # Frame for format selection
    format_frame = ttk.Frame(root, padding=10)
    format_frame.pack(fill='x')

    format_label = ttk.Label(format_frame, text="Select Format:")
    format_label.pack(side='left', padx=(0, 10))

    format_var = tk.StringVar(value="")  # Stores the selected format
    format_menu = ttk.Combobox(
        format_frame, textvariable=format_var, values=[], state='readonly')
    format_menu.pack(side='left', fill='x', expand=True)

    # Frame for save location
    save_frame = ttk.Frame(root, padding=10)
    save_frame.pack(fill='x')

    save_label = ttk.Label(save_frame, text="Save Location:")
    save_label.pack(side='left', padx=(0, 10))

    global save_path_var
    save_path_var = tk.StringVar(value=".")
    save_entry = ttk.Entry(
        save_frame, textvariable=save_path_var, width=40, state='readonly')
    save_entry.pack(side='left', fill='x', expand=True)

    browse_button = ttk.Button(
        save_frame, text="Browse", command=choose_save_path)
    browse_button.pack(side='left', padx=(10, 0))

    # Progress Bar
    progress = ttk.Progressbar(root, length=550, mode='determinate')
    progress.pack(pady=20)

    # Download Button
    download_button = ttk.Button(
        root,
        text="Download Video",
        command=lambda: start_download(
            url_entry.get(),
            progress,
            format_var.get(),
            save_path_var.get()
        )
    )
    download_button.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()


# Run the GUI
if __name__ == "__main__":
    create_gui()
