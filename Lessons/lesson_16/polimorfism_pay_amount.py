class CreditCardPayment:
    def pay(self, amount):
        return f"💳 Знято {amount} грн з кредитної картки (включно з комісією 1%)."

class PayPalPayment:
    def pay(self, amount):
        return f"📱 Проведено безпечний платіж {amount} грн через акаунт PayPal."

class CryptoPayment:
    def pay(self, amount):
        return f"🪙 Перераховано еквівалент {amount} грн у Bitcoin без посередників."

# Функція кошика, яка приймає БУДЬ-ЯКУ платіжну систему
def checkout(payment_method, total_sum):
    # Поліморфний виклик: один наказ — різні дії
    print(payment_method.pay(total_sum))

# Створюємо різні платіжні інструменти
card = CreditCardPayment()
paypal = PayPalPayment()
bitcoin = CryptoPayment()

# Один і той самий процес checkout працює з усіма
checkout(card, 1500)    # Виведе текст для картки
checkout(paypal, 1500)  # Виведе текст для PayPal
checkout(bitcoin, 1500) # Виведе текст для крипти
