import os

import speech_recognition as sr
from speech_recognition import UnknownValueError
import soundfile as sf


class Media:
    r = sr.Recognizer()
    message_text = ""
    message_wav = "./downloads/message_wav.wav"
    message_ogg = "./downloads/message_ogg.ogg"
    message_mp4 = "./downloads/message_mp4.mp4"
    lang = ""

    def reformat(self):
        self.__media_to_text()
        audio_file = sr.AudioFile(self.message_wav)
        try:
            with audio_file as audio:
                content = self.r.listen(audio)
            self.message_text = self.r.recognize_google(content, language=self.lang)
        except UnknownValueError:
            self.message_text = "Слова не распознаны."

    def __media_to_text(self):
        if os.path.exists(self.message_ogg) is True:
            data, samplerate = sf.read(self.message_ogg)
            sf.write(self.message_wav, data, samplerate)
        else:
            os.system(
                'ffmpeg -i {} -acodec pcm_s16le -ar 16000 {}'.format(f"{self.message_mp4}", f"{self.message_wav}")
            )

    def clear(self):
        os.remove(self.message_wav)
        if os.path.exists(self.message_ogg) is True:
            os.remove(self.message_ogg)
        else:
            os.remove(self.message_mp4)
