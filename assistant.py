import sounddevice as sd
from scipy.io.wavfile import write
import whisper
import pyttsx3
import datetime
import colorama
from colorama import Fore, Style

colorama.init()

# تسجيل الصوت
def record_audio(duration=6, fs=44100, filename="recording.wav"):
    print(Fore.CYAN + "[INFO] Start speaking..." + Style.RESET_ALL)
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, recording)
    print(Fore.CYAN + "[INFO] Recording complete." + Style.RESET_ALL)
    return filename

# تحويل النص إلى كلام
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# الردود الذكية
def generate_response(text):
    text = text.lower()
    if "weather" in text:
        return "I cannot check the weather now, but I hope it's sunny!"
    elif "your name" in text:
        return "My name is Python Assistant!"
    elif "hello" in text or "hi" in text:
        return "Hello! How can I help you today?"
    elif "time" in text:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}."
    else:
        return "Sorry, I didn’t understand that. Try asking something else."

# تشغيل البرنامج
def main():
    filename = record_audio()
    
    print(Fore.CYAN + "[INFO] Transcribing..." + Style.RESET_ALL)
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    
    text = result["text"]
    print(Fore.YELLOW + "[YOU SAID] ", text.strip() + Style.RESET_ALL)
    
    response = generate_response(text)
    print(Fore.GREEN + "[ASSISTANT REPLY] ", response + Style.RESET_ALL)

    speak_text(response)

if __name__ == "__main__":
    main()
