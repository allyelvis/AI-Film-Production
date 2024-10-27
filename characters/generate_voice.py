from gtts import gTTS

# Generate audio from script text
text = "I will find you, and I will stop you!"
tts = gTTS(text=text, lang='en')
tts.save("characters/dialogue.mp3")
