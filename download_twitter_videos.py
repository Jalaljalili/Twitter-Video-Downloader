import yt_dlp

def download_videos_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            urls = [line.strip() for line in file if line.strip()]
            
        if not urls:
            print("No URLs found in the file.")
            return
        
        ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',  # Save with video title
            'format': 'bestvideo+bestaudio/best'  # Best quality available
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)
        
        print("Download completed!")
        
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = "twitter_videos.txt"  # Change this to your file path
    download_videos_from_file(file_path)