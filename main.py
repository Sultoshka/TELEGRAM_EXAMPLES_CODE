import webbrowser

import telebot

bot = telebot.TeleBot('6900287057:AAGh87ROoJGRYNgUExmRKurFGsKgb1mciTM')

@bot.message_handler(commands=['site','website'])
def site(message):
    webbrowser.open('https://itproger.com')

@bot.message_handler(commands=['start','main','hello'])
def main(message):
    bot.send_message(message.chat.id,f'Привет, {message.from_user.first_name},{message.from_user.first_name}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>help</b> <em><u>information</u></em>', parse_mode='html')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'Привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name},{message.from_user.first_name}')
    elif message.text.lower() == 'id':
     bot.reply_to(message, f'ID': {message.from_user.id}')
    elif message.text.lower() == '/start':
       bot.send_message(message.chat.id,f'Привет, {message.from_user.first_name},{message.from_user.first_name}')

bot.infinity_polling(none_stop=True)