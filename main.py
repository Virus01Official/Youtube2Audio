import os
import subprocess

def download_video_as_mp3(video_url, output_folder):
    try:
        print(f"Downloading and converting: {video_url}")
        output_template = os.path.join(output_folder, "%(title)s.%(ext)s")
        subprocess.run([
            "yt-dlp",
            "-x",
            "--audio-format", "mp3",
            "-o", output_template,
            video_url
        ], check=True)
        print("Download and conversion complete.")
    except subprocess.CalledProcessError as e:
        print(f"Error processing {video_url}: {e}")

def main():
    # User input
    choice = input("Do you want to convert a single video or a playlist? (video/playlist): ").strip().lower()
    output_folder = input("Enter the output folder path: ").strip()
    os.makedirs(output_folder, exist_ok=True)

    if choice == "video":
        video_url = input("Enter the YouTube video URL: ").strip()
        download_video_as_mp3(video_url, output_folder)
    elif choice == "playlist":
        playlist_url = input("Enter the YouTube playlist URL: ").strip()
        download_video_as_mp3(playlist_url, output_folder)
    else:
        print("Invalid choice. Please type 'video' or 'playlist'.")

if __name__ == "__main__":
    main()
