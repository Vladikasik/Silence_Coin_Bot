def main():
    import telebot
    import var
    import messages
    import keyboard
    import start_disk
    import prsn_inf

    bot = telebot.TeleBot(var.token_of_bot)


    # Функйия которая реагирует на команды
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, messages.start_command,reply_markup=keyboard.markup)

        start_disk.main(message.from_user.first_name,
                        message.from_user.last_name,
                         message.from_user.username)

    @bot.message_handler(commands=['help'])
    def help_message(message):
        bot.send_message(message.chat.id,messages.dk)

    # Функция которая реагирует на текст из кнопок
    @bot.message_handler(func=lambda message: True)
    def main_func(message):
        if message.text == keyboard.bttn_info:
            per = prsn_inf.info(message.from_user.username)
            prsn_inf.dell()
            mes = messages.inf(per)
            bot.send_message(message.chat.id,mes)
            print('Message sent')
        if message.text == keyboard.bttn_info:
            mes = bot.send_message(call.message.chat.id, messages.tr)
            bot.register_next_step_handler(mes,trans)

    def trans(mes):
        return mes.from_user.username, mes.text





    bot.polling(timeout=10)

if __name__ == '__main__':
    main()

