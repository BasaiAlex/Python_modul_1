import os
import json
from my_calc import calculate_bonus, translate

FILE_NAME = 'MyData.txt'

def read_data_from_file():
    if not os.path.exists(FILE_NAME):
        return None
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except (json.JSONDecodeError, FileNotFoundError):
        return None

def write_data_to_file(data):
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)

def main():
    data = read_data_from_file()
    
    if not data:
        # Якщо файл відсутній або дані некоректні
        experience = input("Введіть стаж (кількість років): ")
        salary = input("Введіть розмір зарплати (грн): ")
        language = input("Введіть мову інтерфейсу (uk/en): ")
        
        try:
            experience = int(experience)
            salary = float(salary)
        except ValueError:
            print("Некоректні дані.")
            return
        
        if experience < 0 or experience > 70:
            print("Некоректний стаж. Введіть число від 0 до 70.")
            return
        
        data = {'experience': experience, 'salary': salary, 'language': language}
        write_data_to_file(data)
        print(f"Дані збережено в файл {FILE_NAME}")
        return

    # Якщо дані успішно зчитані
    experience = data['experience']
    salary = data['salary']
    language = data['language']

    # Використовуємо функцію для перекладу
    interface_lang = translate(language)

    print(f"Мова: {interface_lang}")
    print(f"Зарплата: {salary} грн. Стаж: {experience} років.")

    # Розраховуємо надбавку
    bonus_percent, bonus_amount, total = calculate_bonus(experience, salary)
    print(f"Надбавка (%): {bonus_percent}%")
    print(f"Надбавка (грн): {bonus_amount} грн")
    print(f"Всього: {total} грн")

if __name__ == "__main__":
    main()
