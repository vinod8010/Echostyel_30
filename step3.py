import speech_recognition as sr

# Create a recognizer
r = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Speak something... (waiting)")
    r.adjust_for_ambient_noise(source)  # Reduce background noise
    audio = r.listen(source)

try:
    # Try to recognize speech
    text = r.recognize_google(audio)
    print("✅ You said:", text)

except sr.UnknownValueError:
    # If speech was not understood
    print("⚠ Sorry, I could not understand the audio. Please try again.")

except sr.RequestError as e:
    # If API request failed
    print(f"🚫 Could not request results from Google Speech Recognition service; {e}")
