import fsm
import telebot
import keyboards
import ai
import loguru
import yaml
import sys

logger=loguru.logger

try:
    with open("./config.yaml",'r' )as file:
        cfg=yaml.safe_load(file)
        logger.info('Успешно загружен конфиг')
except Exception as e:
    logger.warning('произошла беда({})',str(e))
    input()
    sys.exit(1)

bot_token=cfg['telegram_token']
stater=fsm.FSM()
ai_service=ai.Ai(cfg)
bot=telebot.TeleBot(bot_token)

def handle_def_state(message):
    if message.text == "фото😀":
        stater.set_state(message.chat.id,fsm.image_state)
        bot.send_message(message.chat.id,text='введите ваш запрос',reply_markup=keyboards.keyboard1)
    elif message.text == "текст":   
        stater.set_state(message.chat.id,fsm.text_state) 
        bot.send_message(message.chat.id,text='введите текст',reply_markup=keyboards.keyboard1)
    else:
        return_to_menu(message.chat.id)
    

def handle_image_state(message):
    if message.text=='в меню':
        return_to_menu(message.chat.id)
    else:
        try:
            msg=bot.send_message(chat_id=message.chat.id,text='генерирую')
            image_url=ai_service.generate_image(message.text)
            bot.delete_message(chat_id=message.chat.id,message_id=msg.id)
            bot.send_photo(chat_id=message.chat.id,caption='your photo',photo=image_url)
        except Exception as e:
            bot.send_message(message.chat.id,text=f'когда нибудь потом({str(e)})')

def handle_text_state(message):
    if message.text=='в меню':
        ai_service.clear_dialog(message.chat.id)
        return_to_menu(message.chat.id)
    else:
        msg=bot.send_message(message.chat.id, 'так так так')
        txt=ai_service.generate_text(message.text,message.chat.id)
        msg=bot.edit_message_text(text=txt,chat_id=message.chat.id,message_id=msg.id)

def return_to_menu(chat_id):
    stater.set_state(chat_id,fsm.def_state) 
    bot.send_message(chat_id,"Главное меню",reply_markup=keyboards.keyboard2)

@bot.message_handler(func=lambda message: True)
def om_mes(message):
    # msg_text=message.text
    state=stater.get_state(message.chat.id)
    logger.info(
        "пользователь[{}:{}] отправил сообщение '{}' в состоянии {}",
        message.chat.id,
        message.from_user.first_name,
        message.text,
        state 

    )
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