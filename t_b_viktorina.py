import telebot
import random

# Замените на ваш собственный API токен
API_TOKEN = '*******************************************'

# Создайте объект бота
bot = telebot.TeleBot(API_TOKEN)

# Определите вопросы и ответы
questions_and_answers = [
    ("Как называется самое большое животное в Азии?", "Китайский пандын (Ailuropoda melanoleuca)"),
    ("Как называется самое крупное животное в мире?", "Африка - Слон (Loxodonta africana)"),
    ("Как называется самое маленькое животное в мире?", "Австралия - Микропланктон (Microplankton)"),
    ("Как называется самое быстрое животное в мире?", "Австралия - Морской олень (Mirounga leonina)"),
    ("Как называется самое высокое животное в мире?", "Австралия - Эму (Dromaius novaehollandiae)"),
    ("Как называется самое длинное животное в мире?", "Австралия - Мегадонтозавр (Megadontosaurus giganteus)"),
    ("Как называется самое тяжелое животное в мире?", "Австралия - Мамонт (Mammuthus primigenius)"),
    ("Как называется самое молодое животное в мире?", "Австралия - Голубая птица (Aquila audax)"),
    ("Как называется самое старое животное в мире?", "Австралия - Медведь-материк (Ailuropoda melanoleuca)"),
    ("Как называется самое многочисленное животное в мире?", "Азия - Китайский дракон (Draco draco)"),
    ("Как называется самое мелкое животное в мире?", "Австралия - Микропланктон (Microplankton)"),
    # ... (Продолжайте добавлять вопросы и ответы)
]

# Случайно перемешиваем вопросы и ответы
random.shuffle(questions_and_answers)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_quiz(message):
    bot.send_message(message.chat.id, "Привет! Это викторина по животным. Отвечай на вопросы, и я скажу, правильно ты ответил или нет. Удачи!")
    send_next_question(message.chat.id)

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def answer_question(message):
    global current_question_index
    global score

    if current_question_index < len(questions_and_answers):
        user_answer = message.text.lower()
        correct_answer = questions_and_answers[current_question_index][1].lower()

        if user_answer == correct_answer:
            score += 1
            bot.send_message(message.chat.id, "Правильно!")
        else:
            bot.send_message(message.chat.id, f"Неправильно! Правильный ответ: {correct_answer}")

        current_question_index += 1
        send_next_question(message.chat.id)
    else:
        bot.send_message(message.chat.id, f"Викторина окончена! Ваш счет: {score}/{len(questions_and_answers)}")

# Отправка следующего вопроса
def send_next_question(chat_id):
    global current_question_index

    if current_question_index < len(questions_and_answers):
        question = questions_and_answers[current_question_index][0]
        bot.send_message(chat_id, question)
    else:
        bot.send_message(chat_id, "Викторина окончена!")

# Запуск бота
if __name__ == '__main__':
    current_question_index = 0
    score = 0
    bot.polling()