
 Віртуальне середовище, pip та .gitignore


1. Віртуальне середовище (.venv)

Головне правило: Створюйте окреме середовище .venv у корені кожного конкретного проєкту, а не одне спільне на весь комп’ютер.

 Покроковий алгоритм запуску:


Крок	 Windows (PowerShell)  macOS /  Linux
1. Створення	python -m venv .venv	python3 -m venv .venv
2. Активація	.\.venv\Scripts\Activate.ps1	source .venv/bin/activate
3. Оновлення pip	python -m pip install --upgrade pip	python -m pip install --upgrade pip
4. Встановлення	python -m pip install requests	python -m pip install requests


 Перевірка активації:

Після активації команда python має вказувати на інтерпретатор усередині вашого проєкту. Перевірте це командою:
bash
python -c "import sys; print(sys.executable)"
Use o código com cuidado.
Шлях у результаті обов'язково повинен містити папочку .venv.
• Деактивація: Команда deactivate виходить із середовища, але не видаляє його з диска.
• VS Code: Після створення середовища обов'язково виберіть інтерпретатор саме з вашої папки .venv у налаштуваннях редактора.

2. Керування пакетами через pip

Використання префіксу python -m pip замість простого pip гарантує, що пакет встановиться саме в активне віртуальне середовище поточного інтерпретатора.
• python -m pip list — показати всі встановлені пакети та їх версії.
• python -m pip show requests — відобразити детальну інформацію про конкретний пакет.
• python -m pip uninstall requests — видалити пакет із середовища.
• python -m pip freeze > requirements.txt — записати всі залежності проєкту у файл (для збереження).
• python -m pip install -r requirements.txt — встановити всі залежності з файлу (на іншому ПК чи сервері).


Ось як швидко запустити та перевірити віртуальне середовище:

🚀 Крок 1. Активація (оберіть свою ОС)

• Windows (у терминалі PowerShell):powershell
.\.venv\Scripts\Activate.ps1
Use o código com cuidado.
(Якщо виникає помилка безпеки про "Execution Policy", спершу виконайте команду: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process, а потім знову команду активації).
• macOS / Linux:bash
source .venv/bin/activate
Use o código com cuidado.
Як зрозуміти, що спрацювало? У початку вашого рядка в терміналі з'явиться префікс (.venv). Наприклад: (.venv) PS C:\my_project>.

🔍 Крок 2. Перевірка (чи дійсно Python став «віртуальним»)

Виконайте цю команду в терміналі:
bash
python -c "import sys; print(sys.executable)"
Use o código com cuidado.
• Правильний результат: Ви побачите шлях, який веде всередину папки вашого проєкту, наприклад: C:\Users\...\my_project\.venv\Scripts\python.exe або /Users/.../my_project/.venv/bin/python.
• Неправильний результат (якщо забули активувати): Шлях буде вести до загальносистемного Python, наприклад: C:\Program Files\Python312\python.exe.

🛑 Крок 3. Вихід із середовища

Коли ви завершили роботу над проєктом, просто напишіть:
bash
deactivate
Use o código com cuidado.
Префікс (.venv) зникне, і термінал повернеться до звичайного режиму.
Тепер ваше середовище готове до безпечного встановлення будь-яких пакетів через python -m pip install!