from email.policy import default
def send_email(message, recipient, sender = "university.help@gmail.com"):
    allowed_end = [".com",".ru",".net"]
    proper_rec = False
    proper_sen = False
    proper_input = False
    for i in allowed_end:
        if str(recipient).endswith(i):
            proper_rec = True
        if str(sender).endswith(i):
            proper_sen = True
    if proper_rec == True and proper_sen == True and "@" in str(recipient) and "@" in str(sender):
        proper_input = True
    if proper_input == False:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе.")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
