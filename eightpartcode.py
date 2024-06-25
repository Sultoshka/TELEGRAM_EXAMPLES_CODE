from aiogram import Bot, Dispatcher, executor, types
import config

bot = Bot(config.BOT_TOKEN)
db = Dispatcher(bot)

@db.message_handler(commands=['start'])
async def start(message:types.Message):
    await bot.send_invoice(message.chat.id, 'Покупка курса', 'Покупка курса itProger','invoice', config.PAYMENT_TOKEN, 'USD', [types.LabeledPrice('Покупка курса', 5* 100)])


@db.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async
executor.start_polling(db)