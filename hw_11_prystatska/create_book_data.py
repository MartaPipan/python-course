import csv
from pathlib import Path

def create_book_csv():
    # Тепер шлях веде прямо в папку hw_11_prystatska без додаткової підпапки data
    data_folder = Path.cwd() / "hw_11_prystatska"
    file_path = data_folder / "books.csv"
    
    book_data = [
        {"title": "Гаррі Поттер і філософський камінь", "author": "Джоан Роулінг", "year": "1997", "tags": "фентезі, пригоди"},
        {"title": "1984", "author": "Джордж Орвелл", "year": "1949", "tags": "антиутопія, політика"},
        {"title": "Гобіт, або Туди і назад", "author": "Джон Р. Р. Толкін", "year": "", "tags": "фентезі, пригоди"},
        {"title": "1984", "author": "Джордж Орвелл", "year": "1949", "tags": "антиутопія, класика, політика"},
        {"title": "Колгосп тварин", "author": "Джордж Орвелл", "year": "1945", "tags": "алегорія, saтира"},
        {"title": "Гаррі Поттер і філософський камінь", "author": "Дж. К. Роулінг", "year": "1997", "tags": "фентезі, дитяче"},
        {"title": "Кобзар", "author": "Тарас Шевченко", "year": "1840", "tags": "поезія"}
    ]
    
    headers = ["title", "author", "year", "tags"]
    
    # Відкриваємо і записуємо файл
    with open(file_path, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(book_data)
        
    print(f"Файл успішно створено за шляхом: {file_path}")

if __name__ == "__main__":
    create_book_csv()
