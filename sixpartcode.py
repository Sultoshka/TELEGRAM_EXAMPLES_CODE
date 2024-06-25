from aiogram import Bot, Dispatcher, executor, types

bot = Bot('')
db = Dispatcher(Bot)


@db.message_handler(content_types=['photo']) # commands=['start']
async def start(message: types.Message):
    # await bot.send_message(message.chat.id, 'Hello')
    # await message.answer
    await message.answer('Hello')
    # file = open('/some.png', 'rb')
    # await message.answer_photo(file)


@db.message_handler()
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Site', url='https://itproger.com'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.reply('Hello', reply_markup=markup)



@db.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)

@db.message_handler(commands=['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkp(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Site'))
    markup.add(types.KeyboardButton('Website'))
    await message.answer('Hello', reply_markup=markup)

executor.start_polling(db)