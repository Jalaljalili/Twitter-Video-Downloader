# Twitter-Video-Downloader
This Python script allows users to download videos from Twitter using <mark>yt-dlp</mark>.  The script reads a text file containing Twitter video URLs and downloads them in the best available quality.

##Requirements

### 1. Install Python

Ensure you have Python installed on your system. You can check by running:
```
python3 --version
```

If Python is not installed, install it using:
```
brew install python  # macOS (using Homebrew)
```

### 2. Install yt-dlp

yt-dlp is a powerful media downloader. Install it using:
```
pip3 install yt-dlp
```
Or, if using Homebrew on macOS:
```
brew install yt-dlp
```
### 3. Install ffmpeg (Required for Merging Video and Audio)

ffmpeg is needed for handling multiple format downloads. Install it using:
```
brew install ffmpeg  # macOS
```
Or via pip:
```
pip3 install ffmpeg
```
## How to Use

1. Create a text file (e.g., twitter_videos.txt) and add Twitter video URLs, each on a new line.

2. Run the script with:
```
python3 download_twitter_videos.py
```

3. The videos will be downloaded in the best available quality and saved with their respective titles.


## Script Explanation

1. Reading the File

The script reads the provided file (twitter_videos.txt) and extracts all non-empty lines, treating them as URLs.

```shell
with open(file_path, 'r', encoding='utf-8') as file:
    urls = [line.strip() for line in file if line.strip()]
```

2. Setting Download Options

The script defines yt-dlp options:

```shell
ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',  # Saves video with title as filename
    'format': 'bestvideo+bestaudio/best'  # Best quality available
}
```

3. Downloading the Videos

Using yt-dlp, the script downloads the videos:
```
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(urls)
```

4. Error Handling

* If the file is not found, an error message is displayed.

* If an unexpected error occurs, the script prints the error.

### Troubleshooting

* Command not found: pip → Try pip3 instead.

* ffmpeg not installed error → Install ffmpeg using ```brew install ffmpeg.```

* Download fails → Ensure the Twitter URL is public and accessible.

*  Install Homebrew (If You Don’t Have It) :
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

#### License

This script is provided under the MIT License. Feel free to modify and distribute it.

### Author

Jalal Jalili
