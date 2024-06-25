import telebot

bot = telebot.TeleBot('6900287057:AAGh87ROoJGRYNgUExmRKurFGsKgb1mciTM')

@bot.message_handler(content_types=['Photo'])

bot.polling(non_stop=True)