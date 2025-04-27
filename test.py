import telebot
import keyboards


bot_token='8107806798:AAEnsOnTGTY20awbrC8n_hlWji6TW2Op1Qk'
bot=telebot.TeleBot(bot_token)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg_text=message.text
    if msg_text == "фото😀":
        bot.send_message(message.chat.id,text='а вот фиг',reply_markup=keyboards.keyboard1)
    elif msg_text == "текст":    
        bot.send_message(message.chat.id,text='а вот фиг',reply_markup=keyboards.keyboard1)
    else:
        bot.send_message(message.chat.id,text='давай выбирай',reply_markup=keyboards.keyboard2)   
bot.polling()