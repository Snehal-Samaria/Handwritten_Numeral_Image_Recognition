import pyttsx3

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    return audio

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def save_mp3(text,saveas):
    engine.save_to_file(text,saveas)


