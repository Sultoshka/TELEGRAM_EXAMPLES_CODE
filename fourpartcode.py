import json

import telebot
import requests

bot = telebot.TeleBot('')
API = '5cfe304b0497f430268d3842d8c05f52'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! напиши название вашего города')

@bot.message_handler(content_types=['text'])
def get_weather(message):
   city = message.text.strip().lover()
   res = requests.get('https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}')
   if res.status_code == 200:
       data = json.loads(res.text)
       temp = data['main']['temp']
       bot.reply_to(message, f'Сейчас погода: {temp}')

       image = 'sunny.png' if temp > 5.0 else 'sunny.png'
       file = open('./' + image, 'rb')
       bot.send_photo(message.chat.id, file)
   else:
       bot.reply_to(message, 'город указан не верно')


bot.polling(none_stop=True)