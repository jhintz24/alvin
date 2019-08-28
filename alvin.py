import speech_recognition as sr
from Interpreter import Interpreter
import argparse

if __name__ == "__main__":

    # Parse name of output app
    parser = argparse.ArgumentParser()
    parser.add_argument('-appname', required=True, help='name of app file')
    args = parser.parse_args()
    appName = args.appname

    # Set the voice interpreter
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    # Set interpreter
    interpreter = Interpreter(appName)

    # Start listening and interpreting voice input
    while True:
        voiceInput = ''
        with mic as source:
            print("listening...")
            audio = recognizer.listen(source)

        print("sending input...")
        try:
            voiceInput = recognizer.recognize_google(audio)
            print(voiceInput)
        except sr.UnknownValueError:
            print("did not understand...")

        voiceInput = voiceInput.lower()
        if voiceInput == 'exit':
            break

        interpreter.processInput(voiceInput)
