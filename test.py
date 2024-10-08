from telegram import Bot

BOT_TOKEN = "7260168327:AAEEOvNziECXLf29xfIU9rsr9JqIcmOFR_g"
CHAT_ID = -1002009353137


def main():
    bot = Bot(BOT_TOKEN)
    file_paths = (
        "vmess",
        "vmess",
        "test.py"
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
                caption=f"Total students in {f}: {count}"
            )


if __name__ == "__main__":
    main()
