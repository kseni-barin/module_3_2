def send_email(message,  recipient, *, sender = 'university.help@gmail.com'):
    final_str_list = ['.com', '.ru', '.net']
    final_str_sender = '.' + sender.split('.')[-1]
    final_str_recipient = '.' + recipient.split('.')[-1]
    if '@' not in recipient or final_str_recipient not in final_str_list:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif '@' not in sender or final_str_sender not in final_str_list:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    else:
        if sender == recipient:
            print('Нельзя отправить письмо самому себе!')
        else:
            if sender == 'university.help@gmail.com':
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender ='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender ='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender ='urban.teacher@mail.ru')
send_email('Напоминаю о вебинаре', 'teacher@mailnet', sender ='university.help@gmail.com')