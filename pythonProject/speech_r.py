import speech_recognition
audio = ('hello.wav')
r = speech_recognition.Recognizer()
with speech_recognition.AudioFile(audio) as source :
    audio = r.record(source)
try :
    print('audi file contains' + r.recognize_google(audio))
except speech_recognition.UnknownValueError :
    print('Google failes')