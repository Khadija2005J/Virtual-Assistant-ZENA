import speech_recognition as sr
import traceback

print('speech_recognition version:', sr.__version__)
try:
    mics = sr.Microphone.list_microphone_names()
    print('Available microphones:', mics)
    if not mics:
        print('No microphones detected')
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('Using microphone:', source)
            print('Adjusting for ambient noise (1s)...')
            r.adjust_for_ambient_noise(source, duration=1)
            print('Listening (timeout=5s, phrase_time_limit=5s)...')
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print('Captured audio: bytes=', len(audio.frame_data))
    except Exception:
        print('Error during capture:')
        traceback.print_exc()
except Exception:
    print('General error:')
    traceback.print_exc()
