from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC


audio = ID3('ALELUYA (Alé-Grense Los Justos).mp3')
with open('thumbnail.png', 'rb') as albumart:
    audio['APIC'] = APIC(
        encoding=3,
        mime='image/jpeg',
        type=3, desc=u'Cover',
        data=albumart.read()
    )
audio.save()