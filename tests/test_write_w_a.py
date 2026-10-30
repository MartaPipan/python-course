from pathlib import Path

def test_write_and_append_notes():
    # 1. Задаємо шлях: створити папку "data" в корені проекту та файл "notes.txt" всередині неї
    path = Path.cwd() / "data" / "notes.txt"
    
    # 2. Створюємо папку "data", якщо її ще немає на комп'ютері
    path.parent.mkdir(parents=True, exist_ok=True)
    
    # 3. РЕЖИМ "w" (Запис): Стирає все старе і записує перший рядок
    with path.open("w", encoding="utf-8") as file:
        file.write("Перша нотатка\n")
        
    # 4. РЕЖИМ "a" (Дописування): Не чіпає перший рядок, а додає другий в кінець
    with path.open("a", encoding="utf-8") as file:
        file.write("Друга нотатка\n")
        
    # 5. Перевіряємо, що файл дійсно створився
    assert path.exists() is True
