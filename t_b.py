import telebot

# Вставьте сюда ваш токен от BotFather
API_TOKEN = '7173975915:AAEbj3kd0eIEbqZy6ibU3p82v7Hq8GzT0Yg'

# Создаем объект бота
bot = telebot.TeleBot(API_TOKEN)

# Обработчик всех сообщений
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    bot.reply_to(message, 'Привет, все хорошо')

if __name__ == '__main__':
    # Запускаем бесконечный цикл обработки событий
    bot.polling()