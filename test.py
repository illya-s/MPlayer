# # from playsound import playsound
# import winsound
# from os import path

# file = "C:/Users/Ilya/Music/music/Адонай.mp3"
# winsound.PlaySound(file)

# playsound('C:/Users/Ilya/Music/music/Адонай.mp3')

from pydub import AudioSegment
from pydub.playback import play
 
# for playing mp3 file
song = AudioSegment.from_mp3('C:/Users/Ilya/Music/music/Адонай.mp3')
print('playing sound using  pydub')
play(song)