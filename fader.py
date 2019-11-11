from pydub import AudioSegment
from pydub import effects

sra=input()
_sound = AudioSegment.from_file("/home/nkomarn/Documents/MusicPlayer/music/"+sra+".wav", "wav")
sound = effects.normalize(_sound)
print(_sound.max)
sound2 = sound.fade(from_gain=-120.0, start=0, duration=5000)
sound3 = sound2.fade(to_gain=-120.0, end=0, duration=5000)
sound3.export("/home/nkomarn/Documents/MusicPlayer/musictemp/"+sra+".wav", format="wav")