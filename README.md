# Code decrypting voice and video messages from telegram.

-----------------

## The installation is simple, you can do it yourself, if not, then the problems are not mine

------------------------------------

## Installation
```sudo apt-get install ffmpeg```

```git clone https://github.com/Miffle/voice-video_messages-decoding```

```pip install -r requirements.txt```

Finished with the simple one, the next thing you need to do is open main.py и перейти по ссылке в комментарии. Там следуешь инструкции.

---------------------------
## Error fix
### <b><u>Supported file format but file is malformed.</u></b>
Comment ```_error_check(self._errorcode)``` in 
1) ```def seek(self, frames, whence=SEEK_SET)```
2) ```def _cdata_io(self, action, data, ctype, frames)```

in <b>soundfile.py</b>
### <b><u>ValueError: invalid literal for int() with base 10: 'APP ID'.</u></b>
After first launch you can see "my_account.session" if project folder.

**Change in main.py** 
```
api_id = "APP ID"  
api_hash = "APP HASH"
app = Client("my_account", api_id=api_id, api_hash=api_hash)
```

**To** 

```app = Client("my_account")```

---------------------
You can find me in my telegram channel - https://t.me/ftliwdt