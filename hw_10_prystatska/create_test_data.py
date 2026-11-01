import csv
from pathlib import Path

def generate_test_csv():
    # create 'data'---»'scores.csv'
    data_folder = Path.cwd() / "hw_10_prystatska" / "data"
    file_path = data_folder / "scores.csv"

    data_folder.mkdir(parents=True, exist_ok=True)
    
    test_data = [
        {"student_id": "1", "name": "Олена", "score": "95"},  
        {"student_id": "2", "name": "Данило", "score": "35"},    
        {"student_id": "3", "name": "Назар", "score": "78"},         
        {"student_id": "4", "name": "Марко", "score": "100"}, 
        {"student_id": "5", "name": "Орися", "score": "42"},       
        {"student_id": "6", "name": "Катерина", "score": "0"},
        {"student_id": "7", "name": " Уляна", "score": "74"},         
        {"student_id": "8", "name": "Марія", "score": "-5"}, 
        {"student_id": "9", "name": "Дарина", "score": "-3"},    
        {"student_id": "10", "name": "Влад", "score": "0"},          
        {"student_id": "11", "name": "Марина", "score": "105"},
        {"student_id": "12", "name": "Арсен", "score": "300"},    
        {"student_id": "13", "name": "Захар", "score": "12"},         
        {"student_id": "14", "name": "Віталій", "score": ""}, 
        {"student_id": "15", "name": "Ксенія", "score": "1"},    
        {"student_id": "16", "name": "Роксолана", "score": "70"},          
        {"student_id": "17", "name": "Петро", "score": "not"},      
        {"student_id": "18", "name": "Маркіян"},       
    ]
    
    headers = ["student_id", "name", "score"]
    
    with file_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        
        writer.writeheader()
    
        writer.writerows(test_data)
        
    print (f" Файл створено з використання команди у терміналі: python hw_10_prystatska/create_test_data.py\n за шляхом: {file_path.resolve()}")

if __name__ == "__main__":
    generate_test_csv()
