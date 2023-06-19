from flask import Flask, request
from .helpers import process_audio_chunck_20ms, sum_audio_chunks, check_speech_presence, get_wave_file_duration

app = Flask(__name__)

received_audio_files_500ms = []
all_audio_files = []

@app.route('/receive_audio', methods=['POST'])
def receiver():
    audio_file = request.files.getlist('audio')
    all_audio_files.append(audio_file)
    process_audio_chunck_20ms(audio_file,received_audio_files_500ms)
    combined_audio = sum_audio_chunks(received_audio_files_500ms)

    if len(all_audio_files)==25: #Be sure we have a good 500ms lenth chunk before checking for speech
        contains_speech = check_speech_presence(combined_audio)
        if contains_speech:
            return {'contains_speech': "Speech has ended"}
        else :
            return {'contains_speech': "Speech is ongoing"}
        
    elif get_wave_file_duration(sum_audio_chunks(all_audio_files))>=50: #if max 50 seconds audioreceived return True speech ended
        return {'speech_status': "Speech has ended"}
    
    return {'speech_status': ""}#Return nothing if chunck is not up to 500ms


    