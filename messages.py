start_command = 'Здраствуйте, вы запустили бота SilenceCoin. \n' \
                'Выбирите из меню кнопок нужную вам команду, \n' \
                'далее следуйте за инструкциями.\n' \
                'Чтобы опять вызвать это меню напишите боту /start\n' \
                '\n' \
                'Ссылка на группу ВК: https://vk.com/silence_coin\n' \
                'Ссылка на бота: https://t.me/SilenceCoinBot'
dk = 'Помошь уже тут!.\n' \
     'Введите /start чтобы начать работу с ботом \n' \
     'Если у вас етсь вопросы по работе бота, \n' \
     'задайте их в группе ВК https://vk.com/silence_coin'

tr = 'Чтобы перевести деньги, введите ник \n'\
     'пользователя которому вы хотите перевести денег.'

def inf(prsn):
    fn = prsn['FirstName']
    sn = prsn['SecondName']
    un = prsn['Username']
    bl = prsn['Balance']

    message = ['Имя: ',fn,' ',sn,'\n',
            'Юзернэйм: ', un, '\n',
            'Баланс: ', bl]
    print(''.join(message))
    return ''.join(message)