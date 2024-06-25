from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('')
db = Dispatcher(bot)


@db.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://itproger.com')))
    await message.answer('Привет, мой друг!', reply_markup=markup)

executor.start_polling(db)