# Speech-to-Text
A Python project that records speech, converts it to text using Whisper, generates an AI response with Cohere, and speaks the response aloud.

## Features ✨
- *Speech-to-Text*: Accurate audio transcription using OpenAI's Whisper
- *AI Responses*: Intelligent conversation with Cohere's language model
- *Text-to-Speech*: Natural voice output using gTTS
- *Easy Setup*: Works with standard microphone input

## Requirements 📋
To run this project, you need the following libraries installed:
	•	speech_recognition: For capturing audio from the microphone.
	•	whisper: For transcribing the audio into text.
	•	gtts: For converting text into speech.
	•	cohere: For generating responses based on the transcribed text.
- Python 3.8+
- Microphone (built-in or external)

- Whisper model:
Ensure you have access to the Whisper model (whisper library) installed. You can use whisper for transcribing spoken audio into text.

How It Works:
	1.	Capture Audio:
	•	The program uses the speech_recognition library to capture audio from the microphone.
	•	The microphone listens for a user’s speech and saves the audio to a .wav file.
	2.	Transcribe with Whisper:
	•	The saved audio file is passed to the Whisper model to transcribe the speech into text.
	3.	Generate AI Response:
	•	The transcribed text is sent to Cohere for generating a response based on the user’s speech.
	•	The API returns a short response, which is printed to the console.
	4.	Convert Text to Speech:
	•	The generated response is converted into speech using the gTTS library, and the resulting audio is saved as an MP3 file.
	5.	Play the Response:
	•	The MP3 file containing the AI’s response is played using the os module.

