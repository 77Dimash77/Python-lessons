# # Задача 1. Создайте пользовательский аналог метода map().
# def select(f,col):
#   return [f(x) for x in col]
# def where(f,col):
#   return [x for x in col if f(x)]
# data = [1,2,3,5,8,15,23,38]
# res = select(int,data)
# print(res)
# res = where(lambda x: x%2 ==0,res)
# print(res)
# res = list(select(lambda x: (x, x**2),res))
# print(res)

# # Задача 2. Создайте декоратор, повторяющий функцию заданное количество раз.
# def report_times(n):
#   def our_format(func):
#       def decorator(*args):
#           for i in range(n):
#             for arg in args:
#                 print(f'{arg} + ', end='')
#             print('\b\b= ', end ='')
#             func(*args)
#       return decorator
#   return our_format

# @report_times(3)
# def sum4(a, b, c, d):
#     print(a + b + c +d)
# sum4(4,5,6,7)

# Задача 3. Добавьте в telegram-бота игру «Угадай числа». 
# Бот загадывает число от 1 до 1000. Когда игрок угадывает его, 
# бот выводит количество сделанных ходов.

import telebot
import requests
import random
bot = telebot.TeleBot("6076476961:AAHT0WqAzhucOds7nnTiWV6PUHrTuMDBWDk")
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")
	
# # @bot.message_handler(func=lambda m: True)
# # def echo_all(message):
# # 	bot.reply_to(message, message.text)

# @bot.message_handler(content_types=['text'])
# def greetings(message):
# 	# print(message)
# 	text = message.text
# 	if 'привет' in text:
# 		bot.reply_to(message, f'привет, {message.from_user.first_name}')
# 	elif text == 'погода':
# 		req = requests.get('https://wttr.in/?0T')
# 		bot.reply_to(message,req.text)
# 	elif text == 'котик':
# 		req = requests.get('https://cataas.com/cat')
# 		bot.send_photo(message.from_user.id,req.content)

@bot.message_handler(commands=['start1'])
def start_game(message):
    number = random.randint(1, 1000)
    attempts = 0
    bot.reply_to(message, "Давай сыграем в игру 'Угадай число'! Я загадал число от 1 до 1000. Попробуй угадать!")
    
    @bot.message_handler(func=lambda message: True)
    def guess_number(message):
        nonlocal attempts
        attempts += 1
        try:
            guess = int(message.text)
            if guess == number:
                bot.reply_to(message, f"Поздравляю! Ты угадал число {number} за {attempts} попыток.")
                bot.remove_message_handler(guess_number)
            elif guess < number:
                bot.reply_to(message, "Загаданное число больше.")
            else:
                bot.reply_to(message, "Загаданное число меньше.")
        except ValueError:
            bot.reply_to(message, "Пожалуйста, введи только число.")
    bot.send_message(message.chat.id, "Введи число:")
bot.polling()