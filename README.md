# YouTube Video Downloader

This is a Python-based GUI application for downloading YouTube videos at the highest resolution available. It uses the `yt-dlp` library to handle the video download process and `ttkbootstrap` to create a modern, customizable user interface.

## Features

- Downloads the highest quality video and audio available from YouTube.
- Progress bar to track the video download status.
- Allows you to select the download location on your machine.
- Simple and user-friendly interface.

## Requirements

Before running the application, make sure you have the following installed:

1. **Python 3.6+**
2. **yt-dlp** - A tool for downloading videos from YouTube and other video platforms.
3. **ttkbootstrap** - A modern, themable, and customizable extension of Tkinter.
4. **Tkinter** - Python’s standard GUI package (should come pre-installed with Python).

You can install the required Python libraries with:

```bash
pip install -r requirements.txt
```

## How to Use

Clone this repository or copy the code into a Python file (e.g., `app.py`).

Run the application using Python:

```bash
python app.py
```

The GUI window will open:

- Enter the **YouTube URL** of the video you want to download.
- Click the **Browse** button to choose where the video should be saved.
- Click **Download** to start the download process.
- A progress bar will display the download status.
- Once the download completes, a message will notify you.

## Code Overview

## Key Components

- `progress_hook(d)`: Updates the progress bar based on the download status.
- `download_video()`: Initiates the download using `yt-dlp`, handles user input, and tracks download progress.
- `select_download_path()`: Opens a dialog box for selecting the download folder.
- Tkinter and ttkbootstrap components: Used to build the graphical interface with custom themes and widgets.

## Main Libraries

- `yt-dlp`: A powerful tool for downloading YouTube videos.
- `ttkbootstrap`: Enhances the default Tkinter widgets with a modern look and feel.
- Tkinter: Python's built-in GUI package for creating windows, buttons, text boxes, etc.

## Screenshots

| Component      | Description                                        |
|----------------|----------------------------------------------------|
| **Main Window** | Contains fields for URL input and download path, along with buttons for browsing and starting the download. |
| **Progress Bar** | Shows the download progress as a percentage. |
| **Notifications** | Displays success or error messages upon download completion or failure. |

## Customization

You can easily change the theme of the application by modifying the `themename` argument in the following line of code:

```python
app = ttk.Window(themename="litera")
```

Available themes include `darkly`, `superhero`, `litera`, etc. For more options, see the ttkbootstrap documentation.
