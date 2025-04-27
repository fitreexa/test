import telebot

bot_token='8107806798:AAEnsOnTGTY20awbrC8n_hlWji6TW2Op1Qk'
bot=telebot.TeleBot(bot_token)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id,message.text)
bot.polling()