from mutagen.wavpack import WavPack
from mutagen.id3 import ID3, APIC

def get_cover_art(file_path):
    try:
        audio = WavPack(file_path)
        if 'APIC:' in audio.tags:
            apic = audio.tags.get('APIC:')
            return apic.data
        elif 'APIC' in audio.tags:
            apic = audio.tags.get('APIC')
            return apic.data
        else:
            print("No cover art found.")
            return None
    except Exception as e:
        print("Error:", e)
        return None

file_path = "ALELUYA (Alé-Grense Los Justos).mp3"
cover_art = get_cover_art(file_path)
if cover_art:
    with open("cover.jpg", "wb") as f:
        f.write(cover_art)
    print("Cover art saved as 'cover.jpg'.")