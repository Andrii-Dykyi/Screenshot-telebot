import os
from datetime import datetime
import configparser
import logging

from aiogram import Bot, Dispatcher, executor, types

from screenshooter import make_screenshot
from url import get_url


# Set logging level.
logging.basicConfig(level=logging.INFO)

# Reading config file and get token.
config = configparser.ConfigParser()
config.read("config.ini")
TOKEN = config["TELEGRAM"]["TOKEN"]


# Initialize bot.
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=["start"])
async def start(message: types.Message):
    """Send bot discription."""
    await message.answer(
        "Please, send me a link and I'll send you a screenshot ☝️"
    )


@dispatcher.message_handler()
async def send_screenshot(message: types.Message):
    """Get url and send screenshot to user."""

    # Check if there is at least one link in message.
    if get_url(message.text):
        await message.answer("Link accepted 👍")

        for url in get_url(message.text):
            file_path = os.path.join(
                "temp", str(datetime.now()) + "_screenshot.png"
            )

            await make_screenshot(url, file_path)  # Make scrrenshot.

            # await message.answer_photo(  # Send screenshot like photo
            #     open(file_path, "rb")    # (bad image quality)
            # )

            await message.answer_document(  # Send screenshot like file
                open(file_path, "rb")       # (good image quality)
            )
            os.remove(file_path)  # Remove file.
    else:
        await message.answer(
            "Please, send me a link 😐"
        )
    

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)
