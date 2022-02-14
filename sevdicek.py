from gtts import gTTS
from playsound import playsound

text = "Seni seviyorum ve hep yanında olacağım."
language = "tr"
sound = gTTS(text=text, lang=language, slow=False)
sound.save("sound.mp3")

playsound("sound.mp3")