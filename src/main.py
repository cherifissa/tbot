import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv

from command import show_help, get_input


dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
print(dotenv_path)
load_dotenv(dotenv_path)


def main():
    """
    Handles the initial launch of the program (entry point).
    """
    token = os.getenv("BOT_TOKEN")
    application = Application.builder().token(token).concurrent_updates(True).read_timeout(30).write_timeout(30).build() # noqa
    application.add_handler(CommandHandler('start', show_help))
    application.add_handler(CommandHandler('help', show_help))
    application.add_handler(MessageHandler(filters.TEXT, get_input))
    print("TeleQR instance started!")
    application.run_polling()


if __name__ == '__main__':
    main()
