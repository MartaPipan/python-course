import csv
from pathlib import Path

def create_book_csv():
    data_folder = Path.cwd() / "hw_11_prystatska"
    data_folder.mkdir(parents=True, exist_ok=True) # Переконуємось, що папка існує
    file_path = data_folder / "books.csv"
    
    book_data = [
        {"title": "Тигролови", "author": "Іван Багряний", "year": "1944", "tags": "пригоди, класика", "type": "printed", "pages_count": 320},
        {"title": "Місто", "author": "Валер'ян Підмогильний", "year": "1928", "tags": "модернізм, romance", "type": "printed", "pages_count": 290},
        {"title": "Інтернат", "author": "Сергій Жадан", "year": "2017", "tags": "сучасна проза, війна", "type": "printed", "pages_count": 330},
        {"title": "Фелікс Австрія", "author": "Софія Андрухович", "year": "2014", "tags": "історія, драма", "type": "ebook", "download_url": "https://library.com"},
        {"title": "Танго смерті", "author": "Юрій Винничук", "year": "2012", "tags": "роман, історія", "type": "printed", "pages_count": 480},
        {"title": "Дюна", "author": "Френк Герберт", "year": "1965", "tags": "фантастика, космос", "type": "printed", "pages_count": 600},
        {"title": "Фундація", "author": "Айзек Азімов", "year": "1951", "tags": "наукова фантастика", "type": "ebook", "download_url": "https://scifi-library.org"},
        {"title": "Воно", "author": "Стівен Кінг", "year": "1986", "tags": "жах, трилер", "type": "printed", "pages_count": 1100},
        {"title": "Вбивство у Східному експресі", "author": "Агата Крісті", "year": "1934", "tags": "детектив, класика", "type": "ebook", "download_url": "https://detective.net"},
        {"title": "Убити пересмішника", "author": "Гарпер Лі", "year": "1960", "tags": "драма, класика", "type": "printed", "pages_count": 400},
        {"title": "Володар перснів", "author": "Джон Р. Р. Толкін", "year": "1954", "tags": "фентезі, епос", "type": "printed", "pages_count": 1200},
        {"title": "Марсіанин", "author": "Енді Вейр", "year": "2011", "tags": "фантастика, виживання", "type": "ebook", "download_url": "https://space-books.com"},
    ]
    
    # Модифікуємо кожен рядок: додаємо заповнені поля "download_url"/"pages_count" та "delivery_type"
    for item in book_data:
        if item["type"] == "printed":
            item["download_url"] = "" 
            item["delivery_type"] = f"Друкована книга '{item['title']}' ({item['pages_count']} стор.) буде доставлена поштою або кур'єром."
        elif item["type"] == "ebook":
            item["pages_count"] = "" 
            item["delivery_type"] = f"Електронна книга '{item['title']}' доступна за посиланням: {item['download_url']}"

    headers = ["title", "author", "year", "tags", "type", "pages_count", "download_url", "delivery_type"]
    

    with open(file_path, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(book_data)
        
    print(f"Файл успішно створено за шляхом: {file_path}")

if __name__ == "__main__":
    create_book_csv()
