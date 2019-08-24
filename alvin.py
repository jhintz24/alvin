import speech_recognition as sr
import Interpreter


if __name__ == "__main__":

    # Set the voice interpreter
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    # Set interpreter
    interpreter = Interpreter()

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

        if voiceInput == 'exit':
            break

        interpreter.processInput(voiceInput)
