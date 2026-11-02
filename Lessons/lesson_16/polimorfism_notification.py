class EmailNotification:
    def __init__(self, email_address):
        self.email = email_address

    def send(self, message):
        return f"📧 Надсилаємо Email на {self.email}: {message}"

class SmsNotification:
    def __init__(self, phone_number):
        self.phone = phone_number

    def send(self, message):
        return f"💬 Надсилаємо SMS на номер {self.phone}: {message}"

class TelegramNotification:
    def __init__(self, chat_id):
        self.chat_id = chat_id

    def send(self, message):
        return f"🤖 Надсилаємо повідомлення у Telegram-чат №{self.chat_id}: {message}"

# Функція на сайті, яка сповіщає про безпеку (наприклад, зміну пароля)
def notify_security_event(notification_service, text):
    # Їй байдуже, куди летить інфо, головне — викликати .send()
    print(notification_service.send(text))

# Налаштування різних користувачів
user_mail = EmailNotification("alex@gmail.com")
user_phone = SmsNotification("+380991112233")
user_tg = TelegramNotification(55443322)

alert_text = "Увага! Вхід у ваш акаунт з нового пристрою!"

# Система викликає одну й ту саму функцію
notify_security_event(user_mail, alert_text)
notify_security_event(user_phone, alert_text)
notify_security_event(user_tg, alert_text)
