import csv
from pathlib import Path

"""
• перетворює текст на ціле число;
• ValueError для нечислового тексту;
• ValueError з повідомленням що оцінка поза діапазоном 0–100;
• повертає коректне число без друку.
"""

def parse_score(text: str) -> int:
    try:
        score = int(text)
    except ValueError:
        raise ValueError(f"Некоректне значення: '{text}' (має бути ціле число)")

    if not 0 <= score <= 100:
        raise ValueError(f"Оцінка поза діапазоном 0–100: {score}")  
    return score


"""
    Імпортує та валідує оцінки студентів з CSV.
    • Читає стовпці student_id, name, score 
    • Покроково обробляє рядки
    • FileNotFoundError, KeyError та ValueError (текст / межі 0-100).
    • Зберігає для відхилених рядків: номер, початковий запис та str(error).
    (• Функція enumerate автоматично рахує рядки, починаючи з першого (start=1), і записує номер у змінну index, а дані рядка — у row)
    • 'else' для збереження даних валідації.
    • 'finally'  використовується лише для виведення тех. повідомлення про завершення роботи програми в терміналі
    • Перевіряє припущення програміста через 'assert'
    Повертає tuple: (correct_data = [] rejected_data = [])
    """
def import_scores(file_name: str = "scores.csv"):
    csv_path = Path.cwd() / "hw_10_prystatska" / "data" / file_name
    
    correct_data = []
    rejected_data = []
    
    try:

        with csv_path.open("r", encoding="utf-8", newline="") as file:
            csv_reader = csv.DictReader(file)
            
            if csv_reader.fieldnames and "score" not in csv_reader.fieldnames:
                raise KeyError(f"Некоректне значення: (відсутній стовпець 'score')")
            
            for line_number, student_row in enumerate(csv_reader, start=1):
                # пропускаємо порожній рядок
                if not any(student_row.values()):
                    continue
                # отримуємо оцінку
                student_score = student_row.get("score")
                
                try:
                    if student_score is None:
                        raise KeyError(f"Відсутні дані 'score' для студента у рядку {line_number}")
                    validated_student_score = parse_score(student_score)      
                    
                except ValueError as validation_error:  # "not", "сімдесять",(""), -5 ,105).
                    rejected_data.append({
                        "line": line_number,
                        "name": student_row.get("name"),
                        "student_id": student_row.get("student_id"),
                        "score_value": student_score,
                        "error": f"Обов'язкове числове значення: {validation_error}"
                    })
                except KeyError as syntax_error_in_column_record:
                    rejected_data.append({
                        "line": line_number,
                        "name": student_row.get("name"),
                        "student_id": student_row.get("student_id"),
                        "score_value": "Відсутнє поле",
                        "error": f"Відсутнє обов'язкове заповнення оцінки: {syntax_error_in_column_record}"
                    })
                else:
                    # Якщо все успішно, зберігаємо чисте число в рядок і додаємо в успішні
                    student_row["score"] = validated_student_score
                    correct_data.append(student_row)

    except FileNotFoundError:
        print(f"Файл не знайдено за шляхом: {csv_path}")
        return [], [{"line": "Відсутнє поле", "score_value": "Відсутнє поле", "error": f"Файл {file_name} відсутній"}]
        
    except KeyError as syntax_error_in_column_record:
        print(f"У файлі відсутній стовпець {syntax_error_in_column_record}")
        return [], [{"line": "Заголовок", "score_value": "Відсутнє поле", "error": f"Відсутній стовпець {syntax_error_in_column_record}"}]
        
    finally:
        print(f"Завершено обробку файлу '{file_name}'.")



    for record in correct_data:
        assert 0 <= record["score"] <= 100, f"оцінка має бути від 0 до 100, якщо ні — зупини програму через помилку коду {record['score']}"
        
    return correct_data, rejected_data





if __name__ == "__main__":
    print("ІМПОРТ ОЦІНОК")
    correct_data, rejected_data = import_scores("scores.csv")
    
    print(f"\nПравильні дані: {len(correct_data)}")
    for student in correct_data:
        print(f"   -> [ID: {student['student_id']}] {student['name']}: {student['score']} балів")
        
    print(f"\nВідхилено через помилки: {len(rejected_data)}")
    for bad_row in rejected_data:
        print(f"{bad_row['line']}, Ім'я: {bad_row['name']}, ID: {bad_row['student_id']} (значення '{bad_row['score_value']}'): {bad_row['error']}")
        
    print("\nІмпорт завершено. Файл запущено за командою в терміналі: python hw_10_prystatska/score_import.py\n")