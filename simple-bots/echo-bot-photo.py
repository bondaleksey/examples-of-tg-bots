from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from dotenv import dotenv_values
from aiogram import F


ENV = dotenv_values(".env")
BOT_TOKEN = str(ENV["RUTUBE_HELPER_BOT_TOKEN"])


# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer("Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь")


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer(
        "Напиши мне что-нибудь и в ответ " "я пришлю тебе твое сообщение"
    )


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
async def send_echo(message: Message):
    await message.reply(text=message.text)


async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)




# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands="start"))
dp.message.register(process_help_command, Command(commands="help"))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_echo)

if __name__ == "__main__":
    dp.run_polling(bot)
