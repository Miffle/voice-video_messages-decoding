from pyrogram import Client, filters

import media

api_id = "APP ID"  # visit this page to create your app https://docs.pyrogram.org/start/setup
api_hash = "APP HASH"

app = Client("my_account", api_id=api_id, api_hash=api_hash)


@app.on_message(filters.private)
async def audio_detect(client, message):
    if (message.voice or message.video_note) is not None:
        await media_download(message)
        t_message = media.Media()
        t_message.lang = "ru_RU"  # Can be changed to recognize another language (English - "en-US")
        t_message.reformat()
        await message_send(t_message, message)
        t_message.clear()


async def media_download(message):
    if message.voice is not None:
        await Client.download_media(app, message, "message_ogg.ogg")
    else:
        await Client.download_media(app, message, "message_mp4.mp4")


async def message_send(t_message, message):
    if message.outgoing:
        await Client.edit_message_caption(app, message.from_user.id, message.id,
                                          f"Расшифровка - \n{t_message.message_text}")
    else:
        await Client.send_message(app, message.from_user.id,
                                  f"Расшифровка - \n{t_message.message_text}")


app.run()
