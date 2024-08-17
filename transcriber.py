import speech_recognition as sr


r = sr.Recognizer()
#Convertir audio en texto
class Transcriber:
    def __init__(self):
        pass
        
    #Siempre guarda y lee del archivo audio.mp3
    #Utiliza whisper en la nube :) puedes cambiarlo por una impl local
    def transcribe(self, audio):
        audio.save("audio.mp3")
        Source = open("audio.mp3", "rb")
        with sr.AudioFile(Source) as S:
            audio_file = r.record(source=S)
        try:
            transcript = r.recognize_google_cloud(audio_file, language='es-MX')
            print("Dijiste: " + transcript)
        except:
            print("No te pude entender")
        return transcript.text