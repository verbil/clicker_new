from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('7183402840:AAHikl6aFATmA5RMHKTP28KZJ1U29FuCbqo')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.KeyboardButton("Play! Click!", web_app=WebAppInfo(url='https://verbil.github.io/clicker_ai/')))

	await message.answer("""Привет!
		
Добро пожаловать в новый кликер в телеграме!. Тебе предстоит добывать RCoin. Что это? 

RCoin - новая эра новой эпохи кликеров. Кликай и прокачивай персонажа и получай монеты, за которые в будущем можно получить классные бонусы!""", reply_markup=markup)

executor.start_polling(dp)