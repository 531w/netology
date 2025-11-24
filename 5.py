from datetime import datetime

#Парсит дату смотря на формат газеты
def parse_newspaper_date(newspaper, date_str):
    formats = {
        'The Moscow Times' : '%A, %B %d, %Y',
        'The Guardian' : '%A, %d.%m.%y',
        'Daily News' : '%A, %d %B %Y'
    }

    
    try:
        date_obj = datetime.strptime(date_str, formats[newspaper])
        return date_obj
    except ValueError:
        return None


def main():
    print("Программа для парсинга дат газет")
    print("Доступные газеты: The Moscow Times, The Guardian, Daily News")
    print("Для выхода введите 'q'")

    while True:
        print("\n" + "="*50)

        newspaper = input("Введите название газеты: ").strip()
        if newspaper.lower() == 'q':
            print("Выход из программы")
            break

        if newspaper not in ['The Moscow Times', 'The Guardian', 'Daily News']:
            print("Неизвестная газета, попробуйте снова")
            continue

        #Ввод даты
        date_str = input("Введите дату в формате газеты: ").strip()
        if date_str.lower() == 'q':
            print("Выход из программы")
            break

        #Парсинг даты
        result = parse_newspaper_date(newspaper, date_str)

        if result:
            print(f"Распознанная дата: {result}")
            print(f"Объект datetime: {result}")
        else:
            print("Ошибка: неверный формат даты для указанной газеты")
            print("Попробуйте снова")

if __name__ == "__main__":
    main()