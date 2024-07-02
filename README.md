# YouTube Video Downloader

This Python script allows you to download YouTube videos with various quality options. It uses the `pytube` library to fetch video information and download the selected stream.

## Features

- Download YouTube videos with different quality options
- Display available video and audio streams
- Show download progress and speed
- Allow custom output directory selection

## Prerequisites

Before running this script, make sure you have Python installed on your system. You'll also need to install the required library:
```bash
pip install pytube
```
## Usage


1. Run the script:

```bash
git clone https://github.com/manuemmanuel/Youtube-Downloader.git
cd Youtube-Downloader
python main.py
```
2. Enter the YouTube video URL when prompted.

3. Choose an output directory or press Enter to use the default "downloads" folder.

4. Select from the available download options by entering the corresponding number.

5. The download will start, showing progress and speed.

6. After the download completes, you can enter another URL or quit the program.

## Functions

- `on_progress`: Callback function to display download progress and speed.
- `get_available_streams`: Retrieves and formats available video and audio streams.
- `download_video`: Main function to handle the download process.
- `main`: Manages the user interface and program flow.

## Notes

- The script creates the output directory if it doesn't exist.
- You can quit the program by entering 'q' when prompted for a URL.
- If an error occurs during the download, it will be displayed in the console.

## Disclaimer

This script is for educational purposes only. Be sure to comply with YouTube's terms of service and respect copyright laws when downloading videos.
