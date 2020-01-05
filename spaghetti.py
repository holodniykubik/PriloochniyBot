import telebot
from message_handler import Handler
from counter import Counter
from user_info import User
from randomizer import Randomizer
bot = telebot.TeleBot('1029587727:AAHc2Gyeleo4nnVj66SPpUFkaMgi-9M_JmQ')
message_handler = Handler()
counter = Counter()
users = []


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Pyhnem priloochku?")


@bot.message_handler(commands=['help'])
def help_(message):
    bot.send_message(message.chat.id, "Pyhnem priloochku!")


@bot.message_handler(commands=['reg'])
def reg(message):
    user_info = User(message.from_user.first_name, message.from_user.username, message.from_user.id, message.chat.id)
    user_exists = check_user_exists(user_info.user_id)
    if not user_exists:
        users.append(user_info)
        bot.send_message(message.chat.id, f"Пидрила @{user_info.username} зарегистрировался")
    else:
        bot.send_message(message.chat.id, f"Ебобошенька @{user_info.username} хули ты делаешь? Я же не резиновый, ты уже зарегистрирован. Сходи пыхни прилучку.")


@bot.message_handler(commands=['pidor'])
def pidor(message):
    randomizer = Randomizer(users)
    pidor = randomizer.choose_pidor()
    bot.send_message(message.chat.id, f"Оказывается, что пидор - @{pidor.username}")


def check_user_exists(user_id):
    for user in users:
        if user.user_id == user_id:
            return True
    return False


@bot.message_handler()
def priloochka(message):
    res = message_handler.name_parser(message.text)
    mention_count = counter.mentions()
    if res:
        counter.mention_incr()
        if mention_count == 1:
            bot.send_message(message.chat.id, f"{res['reply']} {res['name']}, ты {res['message']}")
            counter.reset_counter()


bot.polling()
