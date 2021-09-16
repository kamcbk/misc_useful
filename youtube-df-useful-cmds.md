# Useful Commands for youtube-dl

#### Downloading playlists

youtube-dl -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://www.youtube.com/playlist?list=someplaylistREPLACEME -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' --cookies cookies.txt

#### Downloading single videos

youtube-dl --get-filename -o '%(title)s.%(ext)s' XvCMnMUXqzA --restrict-filenames --cookies cookies.txt
