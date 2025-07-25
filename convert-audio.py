import speech_recognition as sr
import whisper
from gtts import gTTS
import os
import cohere

# Initialize recognizer
recognizer = sr.Recognizer()

# Record audio from microphone
with sr.Microphone() as source:
    print("Speak now...")
    recognizer.adjust_for_ambient_noise(source)
    try:
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
    except sr.WaitTimeoutError:
        print("No speech detected!")
        exit()

# Save audio as WAV file
audio_file = "user_audio.wav"
with open(audio_file, "wb") as f:
    f.write(audio.get_wav_data())

# Transcribe with Whisper
model = whisper.load_model("base")
try:
    result = model.transcribe(audio_file, fp16=False)
    user_text = result["text"]
    print(f"You said: {user_text}")

    if not user_text.strip():
        print("No text to respond to!")
        exit()

    # Generate response with Cohere
    co = cohere.Client("YOUR_API_KEY_HERE")  # Replace with your API key
    response = co.generate(
        model="command",
        prompt=f"User said: {user_text}. Respond with a short answer.",
        max_tokens=50
    )
    ai_response = response.generations[0].text.strip()
    print(f"AI Response: {ai_response}")

    # Convert response to speech
    tts = gTTS(text=ai_response, lang='en')
    tts.save("ai_response.mp3")
    os.system("start ai_response.mp3")  # For Windows

except Exception as e:
    print(f"Error: {e}")