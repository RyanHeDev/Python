# convert video to gif

from moviepy.editor import *

video = VideoFileClip("chessvideo.mp4")
video.write_gif("chessvideo.gif")
