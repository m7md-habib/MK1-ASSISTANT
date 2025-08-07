# MK1-ASSISTANT
Personal Assistant Prototype
Voice Assistant Project — Summary and Setup
*Overview*
This project is a simple voice assistant running locally on your Windows PC using Python. It records your voice, transcribes the speech into text using OpenAI’s Whisper model, sends the text to OpenAI’s GPT API for generating a response, then converts the response to speech and plays it back.

*What We Have Done So Far*
Environment Setup
Created and activated a Conda environment named ai_project with required Python packages installed:

sounddevice for audio recording

scipy for audio processing

gtts for text-to-speech conversion

playsound for playing audio replies

openai-whisper for speech recognition (transcription)

Basic Voice Recording
Implemented a Python script to record audio from the microphone and save it as input_audio.wav.

Speech-to-Text Transcription
Used OpenAI Whisper locally to transcribe the recorded audio to text.

Chat Completion Using OpenAI GPT API
Integrated OpenAI's latest ChatCompletion API to generate responses based on the transcribed text.

Text-to-Speech Response
Converted the generated response text to speech audio using gTTS and played the reply using playsound.

*Current Limitations and Issues*
OpenAI API Quota
The project depends on OpenAI’s API, which has a usage quota and may result in RateLimitError when the quota is exceeded.

Audio Playback on Windows
Playing audio with playsound sometimes throws errors related to the media device (MCI errors).

Transcription Accuracy
Whisper transcriptions sometimes contain errors or inaccurate text.

Assistant Intelligence
The assistant currently replies based on GPT responses, but with basic handling and no extended capabilities like checking real-time data or complex commands.

*How to Run*
Activate your Conda environment:

conda activate ai_project

Run the assistant script:

python assistant.py


Speak into your microphone after the prompt. The assistant will record, transcribe, generate a reply, and speak back.

*Possible Future Improvements*
Run a lightweight local language model on your laptop for offline use without API quota limits.

Improve audio playback reliability using alternative libraries (e.g., pygame or pyttsx3).

Add real-time data integration (weather, time, etc.) using external APIs.

Develop a client-server architecture to use your laptop as a voice assistant server accessible by other devices.

result:
image:
<img width="1112" height="641" alt="لقطة شاشة 2025-08-07 083851" src="https://github.com/user-attachments/assets/e0d899d2-9ad0-40dc-a8dd-a7d4744bd8c3" />



<img width="733" height="1056" alt="لقطة شاشة 2025-08-07 083924" src="https://github.com/user-attachments/assets/7d0a3a89-af77-4cec-8015-90e3fe6adc3d" />


vid:

https://youtube.com/shorts/uf_SsOND0tE?feature=shared


