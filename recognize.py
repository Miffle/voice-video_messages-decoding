import os

import speech_recognition as sr
from speech_recognition import UnknownValueError
import soundfile as sf

r = sr.Recognizer()


def reform(voice_ogg, voice_wav):
    data, samplerate = sf.read(voice_ogg)
    sf.write(voice_wav, data, samplerate)


def recognize_voicemessage(voice_ogg, voice_wav, recognized_text):
    reform(voice_ogg, voice_wav)
    audio_file = sr.AudioFile(voice_wav)

    try:
        with audio_file as audio:
            content = r.listen(audio)
        print(r.recognize_google(content, language="ru-RU"), file=open(recognized_text, "w"))
    except UnknownValueError:
        print(f"Слова не распознаны.", file=open(recognized_text, "w"))


def recognize_videomessage(video_mp4, recognized_text, video_wav):
    os.system('ffmpeg -i {} -acodec pcm_s16le -ar 16000 {}'.format(f"{video_mp4}", f"{video_wav}"))
    audio_from_video_file = sr.AudioFile(video_wav)
    try:
        with audio_from_video_file as audio:
            content = r.listen(audio)
        print(r.recognize_google(content, language="ru-RU"), file=open(recognized_text, "w"))
    except UnknownValueError:
        print(f"Слова не распознаны.", file=open(recognized_text, "w"))
