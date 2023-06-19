import os
from pydub import AudioSegment
import speech_recognition as sr
import wave 

def process_audio_chunck_20ms(received_file,list_to_save):
    list_to_save.append(received_file)


def sum_audio_chunks(audio_files):
    combined_audio = AudioSegment.empty()
    for audio_file in audio_files:
        audio = AudioSegment.from_file(audio_file)
        combined_audio += audio
    return combined_audio

def check_speech_presence(audio):
    recognizer = sr.Recognizer()
    audio.export('tempC.wav', format='wav')  # Export combined audio as temporary WAV file
    with sr.AudioFile('temp.wav') as source:
        audio_data = recognizer.record(source)
    os.remove('temp.wav')  # Remove temporary WAV file
    try:
        recognized_text = recognizer.recognize_google(audio_data)
        return True  # Speech detected
    except sr.UnknownValueError:
        return False  # No speech detected
    
def get_wave_file_duration(audios_combined):
    audios_combined.export('tempB.wav', format='wav')
    with wave.open('tempB.wav', 'rb') as wav_file:
        frames = wav_file.getnframes()
        frame_rate = wav_file.getframerate()
        duration = frames / float(frame_rate)
    return duration


