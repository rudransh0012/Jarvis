import speech_recognition as sr
import webbrowser
import subprocess
from time import sleep
import datetime
import pyttsx3
import random
import os
import time

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.setup_voice()
        
    def setup_voice(self):
        """Configure the voice properties"""
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)  # Change index for different voices
        self.engine.setProperty('rate', 160)  # Speaking speed
        self.engine.setProperty('volume', 0.9)  # Volume level

    def speak(self, text):
        """Make the assistant speak with personality"""
        print(f"Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def greet(self):
        """Greet the user based on time of day"""
        hour = datetime.datetime.now().hour
        if 5 <= hour < 12:
            greeting = random.choice([
                "Good morning sunshine! Ready to conquer the day?",
                "Rise and shine! What's on the agenda today?",
                "Top of the morning to you!"
            ])
        elif 12 <= hour < 17:
            greeting = random.choice([
                "Good afternoon! How's your day going?",
                "Afternoon boss! What can I do for you?",
                "Hello there! Need any assistance?"
            ])
        elif 17 <= hour < 21:
            greeting = random.choice([
                "Good evening! How can I help you relax?",
                "Evening commander! What's the plan?",
                "Hello night owl! Burning the midnight oil?"
            ])
        else:
            greeting = random.choice([
                "Working late I see! How can I assist?",
                "You're up late! Everything okay?",
                "It's getting late, but I'm here to help"
            ])
        
        self.speak(greeting)
        time.sleep(1)
        self.speak("I can open YouTube, WhatsApp, tell you the time, or just chat. What would you like?")

    def recognize_speech(self):
        """Listen for user commands"""
        with sr.Microphone() as source:
            print("\nListening... (say 'help' for options)")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=5)
                command = self.recognizer.recognize_google(audio).lower()
                print(f"You: {command}")
                return command
            except sr.UnknownValueError:
                error_msg = random.choice([
                    "I heard that, but I didn't understand it",
                    "Could you repeat that please?",
                    "My ears must be clogged, say that again?"
                ])
                self.speak(error_msg)
                return None
            except sr.RequestError:
                self.speak("Sorry, my speech service is having issues")
                return None
            except Exception as e:
                self.speak("Oops! Something went wrong")
                print(f"Error: {e}")
                return None

    def execute_command(self, command):
        """Process and execute user commands"""
        if not command:
            return True
            
        if 'youtube' in command:
            response = random.choice([
                "Opening YouTube for your viewing pleasure!",
                "Let's see what's trending on YouTube!",
                "Time for some videos!"
            ])
            self.speak(response)
            webbrowser.open("https://www.youtube.com")
            
        elif 'whatsapp' in command:
            response = random.choice([
                "Opening WhatsApp, who are we messaging today?",
                "Let's see who's online on WhatsApp!",
                "WhatsApp coming right up!"
            ])
            self.speak(response)
            webbrowser.open("https://web.whatsapp.com")
            
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            self.speak(f"The current time is {current_time}")
            
        elif 'date' in command:
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            self.speak(f"Today is {current_date}")
            
        elif 'thank you' in command or 'thanks' in command:
            self.speak(random.choice([
                "You're very welcome!",
                "Happy to help!",
                "Anytime!"
            ]))
            
        elif 'how are you' in command:
            self.speak(random.choice([
                "I'm just bits and bytes, but functioning well! How about you?",
                "I'm always happy when helping you!",
                "I don't have feelings, but my circuits are buzzing with excitement!"
            ]))
            
        elif 'help' in command:
            self.speak("I can open YouTube or WhatsApp, tell you the time or date, or just chat. Try saying 'open YouTube' or 'what time is it?'")
            
        elif 'exit' in command or 'quit' in command or 'goodbye' in command:
            self.speak(random.choice([
                "Goodbye! Come back soon!",
                "Signing off!",
                "Until next time!"
            ]))
            return False
            
        else:
            self.speak(random.choice([
                "I'm not sure I can do that yet, but I'm learning!",
                "Interesting request, but I'm limited to YouTube, WhatsApp, and basic info right now",
                "Let's stick to what I know for now"
            ]))
            
        return True

def main():
    assistant = VoiceAssistant()
    os.system('cls' if os.name == 'nt' else 'clear')
    assistant.speak("Initializing personal assistant...")
    time.sleep(1)
    assistant.greet()
    
    running = True
    while running:
        command = assistant.recognize_speech()
        running = assistant.execute_command(command)
        time.sleep(1)

if __name__ == "__main__":
    main()