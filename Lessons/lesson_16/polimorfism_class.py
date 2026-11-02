class TextReport:
    def render(self):
        return "Текстовий звіт"

class CsvReport:
    def render(self):
        return "name,score"

# Створимо ще один третій клас, який взагалі не пов'язаний з попередніми,
# але також має метод render()
class HtmlReport:
    def render(self):
        return "<h1>Звіт у форматі HTML</h1>"

def show(report):
    # Функції байдуже на клас, їй потрібен лише метод .render()
    print(report.render())

# Створюємо об'єкти
txt = TextReport()
csv = CsvReport()
html = HtmlReport()

# Викликаємо одну й ту саму функцію для абсолютно різних класів:
show(txt)   # Виведе: Текстовий звіт
show(csv)   # Виведе: name,score
show(html)  # Виведе: <h1>Звіт у форматі HTML</h1>
