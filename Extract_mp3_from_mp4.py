import moviepy
import moviepy.editor
video = moviepy.editor.videofileClip(**)
audio = video.audio
audio.write_audiofile('new_audio.mp3')