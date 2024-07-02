from pytube import YouTube
import os
import sys
import time

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    
    current_time = time.time()
    if not hasattr(on_progress, 'start_time'):
        on_progress.start_time = current_time
    elapsed_time = current_time - on_progress.start_time
    if elapsed_time > 0:
        download_speed = bytes_downloaded / (1024 * 1024 * elapsed_time)
    else:
        download_speed = 0

    sys.stdout.write(f"\rProgress: {percentage:.2f}% | Speed: {download_speed:.2f} MB/s")
    sys.stdout.flush()

def get_available_streams(yt):
    streams = []
    for stream in yt.streams.filter(progressive=True):
        streams.append({
            'itag': stream.itag,
            'resolution': stream.resolution,
            'file_type': stream.mime_type.split('/')[1],
            'fps': stream.fps,
            'type': 'Video + Audio'
        })
    for stream in yt.streams.filter(only_audio=True):
        streams.append({
            'itag': stream.itag,
            'resolution': 'Audio Only',
            'file_type': stream.mime_type.split('/')[1],
            'fps': 'N/A',
            'type': 'Audio'
        })
    return streams

def download_video(url, output_path="downloads"):
    try:
        # Create a YouTube object
        yt = YouTube(url, on_progress_callback=on_progress)

        # Get available streams
        streams = get_available_streams(yt)

        if not streams:
            print("No downloadable streams available.")
            return
          
        print("\nAvailable download options:")
        for i, stream in enumerate(streams, 1):
            print(f"{i}. {stream['type']} - Resolution: {stream['resolution']}, "
                  f"Format: {stream['file_type']}, FPS: {stream['fps']}")

        while True:
            choice = input("\nSelect option number: ")
            try:
                choice = int(choice)
                if 1 <= choice <= len(streams):
                    selected_stream = yt.streams.get_by_itag(streams[choice - 1]['itag'])
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        print(f"\nDownloading: {yt.title}")
        print(f"Selected option: {streams[choice - 1]['type']} - "
              f"Resolution: {streams[choice - 1]['resolution']}, "
              f"Format: {streams[choice - 1]['file_type']}, "
              f"FPS: {streams[choice - 1]['fps']}")
        
        selected_stream.download(output_path)
        print("\nDownload completed!")

    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

def main():
    while True:
        url = input("\nEnter the YouTube video URL (or 'q' to quit): ")
        
        if url.lower() == 'q':
            break

        output_path = input("Enter the output directory (press Enter for default 'downloads'): ")
        if not output_path:
            output_path = "downloads"

        download_video(url, output_path)

if __name__ == "__main__":
    main()
