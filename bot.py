from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


from config import Config




config = Config()
bot = Bot(token=config.SECRET_KEY)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hello!\nText me smth")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("I am echo-bot. Text me something \
                                                and I will send that back")


@dp.message_handler()
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)





if __name__ == '__main__':
    executor.start_polling(dp)