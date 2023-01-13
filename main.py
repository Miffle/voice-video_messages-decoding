import os

from pyrogram import Client, filters
import recognize


api_id = "APP ID"  # visit this page to create your app https://docs.pyrogram.org/start/setup
api_hash = "APP HASH"

app = Client("my_account", api_id=api_id, api_hash=api_hash)


VOICE_OGG = "./downloads/voice.ogg"
VIDEO_MP4 = "./downloads/video.mp4"
RECOGNIZED_TEXT_FILE = "./downloads/text.txt"
VOICE_WAV = "./downloads/voice.wav"
VIDEO_WAV = "./downloads/video.wav"


def audio_clearing():
    os.remove(VOICE_OGG)
    os.remove(RECOGNIZED_TEXT_FILE)
    os.remove(VOICE_WAV)


def video_clearing():
    os.remove(VIDEO_MP4)
    os.remove(RECOGNIZED_TEXT_FILE)
    os.remove(VIDEO_WAV)


async def progress(current, total):
    print(f"{current * 100 / total:.1f}%")


@app.on_message(filters.private)
async def audio_detect(client, message):
    if message.voice is not None:
        await Client.download_media(app, message, "voice.ogg", progress=progress)
        recognize.recognize_voicemessage(VOICE_OGG, VOICE_WAV, RECOGNIZED_TEXT_FILE)
        voice_text = open(RECOGNIZED_TEXT_FILE, "r+").read()
        if message.outgoing:
            await Client.edit_message_caption(app, message.from_user.id, message.id,
                                              f"Расшифровка голосового - \n{voice_text}")

        else:
            await Client.send_message(app, message.from_user.id,
                                      f"Расшифровка голосового - \n{voice_text}")
        audio_clearing()
    elif message.video_note is not None:
        await Client.download_media(app, message, "video.mp4", progress=progress)
        recognize.recognize_videomessage(VIDEO_MP4, RECOGNIZED_TEXT_FILE, VIDEO_WAV)
        video_text = open(RECOGNIZED_TEXT_FILE, "r+").read()
        await Client.send_message(app, message.from_user.id,
                                  f"Расшифровка круга - \n{video_text}")
    video_clearing()


app.run()
