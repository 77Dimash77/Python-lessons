# Задача 1. Напишите бота для техподдержки.
# Бот должен записывать обращения пользователей в файл.
# Задача 2. Напишите программу, которая позволяет считывать из
# файла вопрос, отвечать на него и отправлять ответ 
# обратно пользователю.

# Данный бот решает две эти задачи


import telebot
bot = telebot.TeleBot("----")

@bot.message_handler(content_types=['text'])
def send_welcome(message):
	data = open('Vopros.txt', mode='a',encoding='utf-8')
	text = f'{message.from_user.id}: {message.text}\n'
	data.write(text)
	data.close()
	vopros = text.split(':')
	otvet = 'все нормально' # менять ответ здесь
	bot.send_message(vopros[0],f'вы спросили:{vopros[1]}')
	bot.send_message(vopros[0],f'я ответил:{otvet}')

bot.polling()