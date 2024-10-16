from telegram import Bot
import datetime
from datetime import date
import pytz

BOT_TOKEN = "7260168327:AAEEOvNziECXLf29xfIU9rsr9JqIcmOFR_g"
CHAT_ID = -1002009353137
current_time = datetime.datetime.now(pytz.timezone('Asia/Jakarta'))
today = date.today()

def main():
    bot = Bot(BOT_TOKEN)
    file_paths = (
        "vmess",
    )

    for f in file_paths:
        with open(f, "rb") as fin:
            count = len(fin.readlines())
            # After the len(fin.readlines()) file's current position
            # will be at the end of the file. seek(0) sets the position
            # to the begining of the file so we can read it again during
            # sending.
            fin.seek(0)
            bot.send_document(
                CHAT_ID,
                document=fin,
                # Up to 1024 characters.
                # https://core.telegram.org/bots/api#inputmediadocument
                caption=f"Main SubApi: https://github.com/freetomaid/5412/raw/refs/heads/main/{f} \n\n API Archive (this file): https://github.com/freetomaid/5412/raw/refs/heads/main/{f}_{today}\n\n Total Accounts: {len(fin.readlines())}\n\n Updated on: {current_time}"
            )


if __name__ == "__main__":
    main()
