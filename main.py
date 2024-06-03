from aiogram import Bot, Dispatcher, executor, types
from config import TELEGRAM_API
from keyboards.keyboard import get_keyboard1, get_keyboard2
from keyboards.key_inline import k_inl

bot = Bot(token=TELEGRAM_API)
dp = Dispatcher(bot)


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда для того, чтобы загрузить бота'),
    ]
    await bot.set_my_commands(commands)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Привет я бот', reply_markup=get_keyboard1())


@dp.message_handler(lambda message: message.text == 'Отправь фото Леди Гаги')
async def buttom_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://celebitchy.com/wp-content/uploads/2018/09/wenn35401415.jpg', caption='Леди Гага (настоящее имя — Стефани Джоанна Анджелина Джерманотта) — американская певица, автор песен и актриса. Родилась 28 марта 1986 года в Нью-Йорке.', reply_markup=k_inl())


@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def buttom_2_click(message: types.Message):
    await message.answer('Вы можете увидеть фото Большой мамочки', reply_markup=get_keyboard2())


@dp.message_handler(lambda message: message.text == 'Отправь фото Большой мамочки')
async def buttom_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://images2.alphacoders.com/799/thumb-1920-799192.jpg', caption='В ролях Мартин Лоуренс — Малкольм Тёрнер / Большая Мамочка')


@dp.message_handler(lambda message: message.text == 'Назад')
async def buttom_4_click(message: types.Message):
    await message.answer('Вы вернулись назад', reply_markup=get_keyboard1())


async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
