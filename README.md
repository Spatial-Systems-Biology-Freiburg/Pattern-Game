# Pattern Games
A collection of python scripts to model games for students.
These games should be able to display some form of pattern.

## Create a Video
First execute the python script
```bash
mkdir out
python chessboard_1d.py
```
Then use ffmpeg as so
```bash
ffmpeg -y -pattern_type glob -i "out/*.png" -c:v libx264 -b:v 5000k -pass 1 -an -f mp4 movie.mp4
```
