import telebot
import datetime

bot = telebot.TeleBot("6843131318:AAH6FYTwfDNLJQ3H9jhg5RdYi7XqR93ePVg")

keybord = telebot.types.ReplyKeyboardMarkup(True)
keybord.row("Один", "Два")
keybord.row("Дата", "Время", "День недели")
@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Привет", reply_markup=keybord)
@bot.message_handler(content_types=["text"])
def send_text(message):
    if message.text.lower() == "один":
        bot.send_message(message.chat.id, "1")
    elif message.text.lower() == "два":
        bot.send_message(message.chat.id, "2")
    elif message.text.lower() == "дата":
        bot.send_message(message.chat.id, str(datetime.date.today()))
    elif message.text.lower() == "время":
        bot.send_message(message.chat.id, str(datetime.datetime.now().strftime("%H:%M:%S")))
    elif message.text.lower() == "день недели":
        bot.send_message(message.chat.id, str(datetime.datetime.now().strftime("%A")))

bot.polling()
