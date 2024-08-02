#Creating a Artificial Assistent can be a good start for pythonists .
#first prototype 
import pyttsx3

def init_engine(rate=150):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    
    # Get the current speaking rate
    current_rate = engine.getProperty('rate')
    print(f"Current speaking rate: {current_rate}")
    
    # Set the new speaking rate
    engine.setProperty('rate', rate)
    print(f"New speaking rate: {rate}")
    
    return engine

def speak_text(engine, text):
    engine.say(text)
    engine.runAndWait()

# Initialize the engine with the desired speech rate
engine = init_engine(rate=150)  # Adjust the rate value as needed

# Test the speech
speak_text(engine, "Hello, I am Jarvis. How can I assist you today?")
