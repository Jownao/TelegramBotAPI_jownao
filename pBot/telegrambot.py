import telebot
from telebot import types
chave = "2124891518:AAESZiOYt_FMVHxGU8nuBc3DO2IuH9vLsBc"

bot = telebot.TeleBot(chave) 

@bot.message_handler(commands=["badalo"])
def responder(mensagem):
    bot.reply_to(mensagem,"badalado em você")

@bot.message_handler(commands=["redes"])
def responder(mensagem):
    bot.reply_to(mensagem,"Jownao se encontra atualmente nessas redes sociais:\n"+
                          "Instagram: instagram.com/jownao\n"+
                          "Twitch: twitch.tv/jownao\n"+
                          "Github: github.com/Jownao")

@bot.message_handler(commands=["amigos"])
def responder(mensagem):
    bot.reply_to(mensagem,"Amigos:\n"+
                          "Carlo\nRulio\nVicsk\nAlbert\nzaboyz ltda")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message == "oi":
        bot.reply_to(message, "Iae de boa ?")
    else:
	    bot.reply_to(message, message.text)






chat_id = "798429701"

# or add KeyboardButton one row at a time:
markup = types.ReplyKeyboardMarkup()
itembtna = types.KeyboardButton('Badalo')
itembtnv = types.KeyboardButton('de')
itembtnc = types.KeyboardButton('Sino')
itembtnd = types.KeyboardButton('Macho')
itembtne = types.KeyboardButton('Veio')
markup.row(itembtna, itembtnv)
markup.row(itembtnc, itembtnd, itembtne)
bot.send_message(chat_id, "Escolha oque desejar meu caro:", reply_markup=markup)

bot.polling()