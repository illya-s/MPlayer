from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC

def get_title(src):
    audio = EasyID3(src)
    if 'title' in audio:
        title = audio['title'][0]
    else:
        title = src.split("\\")[-1]
    return title

def get_artist(src):
    audio = EasyID3(src)
    if 'artist' in audio:
        artist = audio['artist'][0]
    else:
        artist = "Unknown Artist"
    return artist


def get_cover(src):
    audio = MP3(src, ID3=ID3)

    if 'APIC:' in audio:
        artwork = audio['APIC:'].data
        return artwork
    else:
        return None