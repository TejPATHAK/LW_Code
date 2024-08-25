pip install gtts

from gtts import gTTS

# Text that you want to convert to audio
text = "Hello! This is a text-to-audio conversion example using Python."

# Specify the language for the conversion
language = 'en'


tts = gTTS(text=text, lang=language, slow=False)

# Save the audio file
audio_file = 'output.mp3'
tts.save(audio_file)

print(f"Audio file saved as {audio_file}")
