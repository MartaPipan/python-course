import csv
from pathlib import Path

attendance_dir = Path.cwd() / "hw_09_prystatska" / "data" 

# Ств. структуру автоматично
attendance_dir.mkdir(parents=True, exist_ok=True)

# шлях до CSV, щоб там створити
csv_path = attendance_dir / "attendance.csv"

# запис
data_to_save = [
    {"name": "Олена", "group": "КН-11", "attended": "12", "total": "10,14,8,10,5"},
    {"name": "Марко, молодший", "group": "КН-11", "attended": "10", "total": "10,14,12"},
    {"name": "Катерина", "group": "КН-11", "attended": "3", "total": "10,7,4"},
    {"name": "Марія", "group": "КН-12", "attended": "74", "total": "16,7,13,14,3"},
    {"name": "Марина", "group": "КН-12", "attended": "15", "total": "10"},
    {"name": "Віталій", "group": "КН-10", "attended": "10", "total": "0"},
    {"name": "Петро", "group": "КН-10", "attended": "not", "total": " "}, 
    {"name": "Мар'ян", "group": "К", "attended": "0 ", "total": " 100,11,сімдесять"}, 
    {"name": "Тетяна", "group": "", "attended": " ", "total": "19,11,17"}, 
    {"name": "Влад", "group": "КН-12", "attended": "1", "total": "17,19,3"}, 
    {"name": " ", "group": "КН-12", "attended": " ", "total": " "}, 
    {"name": "Мар'яна", "group": "КН-11", "attended": "30", "total": "20,20"},   
    {"name": "Тарас", "group": "КН-11", "attended": "74", "total": "20,13,13,13,20,13"},    
    {"name": "Надія", "group": "КН-12", "attended": "74", "total": "20,19,20,20,20"},
    {"name": " ", "group": " ", "attended": " ", "total": " "}, 
    {"name": "Софія", "group": "КН-10", "attended": "74", "total": "20"}, 
]

#  Запис у нову папку
with csv_path.open("w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "group", "attended", "total"])
    writer.writeheader()
    writer.writerows(data_to_save)

print(f" Папку створено за шляхом: {attendance_dir}")
print(f" Файл записано сюди за командою у терміналі 'python hw_09_prystatska/create_structure_hw_09.py': {csv_path}")

