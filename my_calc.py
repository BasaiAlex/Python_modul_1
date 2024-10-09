
def calculate_bonus(experience, salary):
    if 2 <= experience < 5:
        bonus_percent = 2
    elif 5 <= experience < 10:
        bonus_percent = 5
    elif experience >= 10:
        bonus_percent = 10
    else:
        bonus_percent = 0
    
    bonus_amount = salary * bonus_percent / 100
    total = salary + bonus_amount
    return bonus_percent, bonus_amount, total

def translate(language_code):
    languages = {
        'uk': 'Українська',
        'en': 'English'
    }
    return languages.get(language_code, 'Українська')  # За замовчуванням українська
