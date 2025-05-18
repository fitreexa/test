import fsm
import telebot
import keyboards

bot_token='8107806798:AAEnsOnTGTY20awbrC8n_hlWji6TW2Op1Qk'
stater=fsm.FSM()
bot=telebot.TeleBot(bot_token)

def handle_def_state(message):
    if message.text == "фото😀":
        stater.set_state(message.chat.id,fsm.image_state)
        bot.send_message(message.chat.id,text='а вот фиг',reply_markup=keyboards.keyboard1)
    elif message.text == "текст":   
        stater.set_state(message.chat.id,fsm.text_state) 
        bot.send_message(message.chat.id,text='а вот фиг',reply_markup=keyboards.keyboard1)
    else:
        return_to_menu(message.chat.id)
    

def handle_image_state(message):
    if message.text=='в меню':
        return_to_menu(message.chat.id)
    else:
        #TODO
        bot.send_message(message.chat.id,text='когда нибудь потом')

def handle_text_state(message):
    if message.text=='в меню':
        return_to_menu(message.chat.id)
    else:
        #TODO
        bot.send_message(message.chat.id,text='когда нибудь потом')

def return_to_menu(chat_id):
    stater.set_state(chat_id,fsm.def_state) 
    bot.send_message(chat_id,"Главное меню",reply_markup=keyboards.keyboard2)

@bot.message_handler(func=lambda message: True)
def om_mes(message):
    # msg_text=message.text
    state=stater.get_state(message.chat.id)
    if state == fsm.def_state:
        handle_def_state(message)
    elif state == fsm.image_state:
        handle_image_state(message)    
    elif state == fsm.text_state:
        handle_text_state(message)
    else:
        stater.set_state(message.chat.id,fsm.def_state)
        bot.send_message(message.chat.id,text='я не понял вашей команды',reply_markup=keyboards.start)
bot.polling()