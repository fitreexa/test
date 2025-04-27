import telebot
button1=telebot.types.KeyboardButton(text='фото😀')
button2=telebot.types.KeyboardButton(text='текст')
button3=telebot.types.KeyboardButton(text='в меню')

keyboard1=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard2=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard2.add(button1,button2)
keyboard1.add(button3)
