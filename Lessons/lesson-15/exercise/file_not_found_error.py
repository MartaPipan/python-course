# Скрипт перехоплює суто відсутність файлу на диску. 

from pathlib import Path

def read_config_file():
    file_path = Path.cwd() / "config.txt"
    
    try:
        # Спроба відкрити та прочитати вміст файлу
        with file_path.open("r", encoding="utf-8") as file:
            print(file.read())
            
    except FileNotFoundError:
        # Спрацює ТІЛЬКИ якщо файлу фізично немає в папці
        print(f"ℹ Дружнє повідомлення: На жаль, файл за адресою '{file_path.name}' не знайдено. "
              f"Перевірте, будь ласка, чи створили ви його у правильній теці.")

read_config_file()
