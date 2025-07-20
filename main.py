import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()


def speak(text):
    """Speak the provided text."""
    engine.say(text)
    engine.runAndWait()


def processCommand(command):
    """Process recognized command and perform actions."""
    command = command.lower()

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "exit" in command or "quit" in command or "stop" in command:
        speak("Goodbye! Have a nice day.")
        exit()
    else:
        speak("Sorry, I didn't understand that. Please try again.")


if __name__ == "__main__":
    speak("Hey ma'am, how may I help you?")

    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("\nListening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

                print("Recognizing...")
                command = recognizer.recognize_google(audio)
                print(f"You said: {command}")

                processCommand(command)

        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
        except sr.UnknownValueError:
            print("Could not understand the audio. Please speak clearly.")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
