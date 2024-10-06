from telegram import Bot, InputMediaDocument
import datetime
from datetime import date
import pytz

BOT_TOKEN = "7260168327:AAEEOvNziECXLf29xfIU9rsr9JqIcmOFR_g"
CHAT_ID = -1002345920504
current_time = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
today = today = date.today()

def main():
    bot = Bot(BOT_TOKEN)
    file_paths = (
        "vmess",
    
    )
    # From 2 to 10 items in one media group
    # https://core.telegram.org/bots/api#sendmediagroup
    media_group = list()
    for f in file_paths:
        with open(f, "rb") as fin:
            # Up to 1024 characters.
            # https://core.telegram.org/bots/api#inputmediadocument
            caption = f"Main SubApi: https://api.vmess.free.nf/{f} \n\n API Archive (this file): https://api.vmess.free.nf/{f}_{today}\n\n Total Accounts: {len(fin.readlines())}\n\n Updated on: {current_time}"
            # After the len(fin.readlines()) file's current position
            # will be at the end of the file. seek(0) sets the position
            # to the begining of the file so we can read it again during
            # sending.
            fin.seek(0)
            media_group.append(InputMediaDocument(fin, caption=caption))

    bot.send_media_group(CHAT_ID, media=media_group)


if __name__ == "__main__":
    main()
