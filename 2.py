#1
'''print('Если хотите остановиться введите "stop"')
while True:
    word = input('Введите слово:')
    
    if not word:
        print('Вы не ввели слово, попробуйте заново или же напишите "stop"')
        continue

    elif ' ' in word:
        print('Проверьте вдруг вы поставили пробел после слова, если нет, то вы ввели предложение, а не слово попробуйте ещё раз или же напишите "stop"')    
        continue

    elif word == 'stop':
        break
    
    else:
        i = len(word) #кол-во об-ов
        m = i // 2

        if i % 2 == 0: #чёт
            print(word[m-1:m+1])
        else: #нечёт
            print(word[m])'''
    


#2 
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']


def find_perfect(boys,girls):
    if not boys and not girls:
        return "Оба списка пустые!"
    elif not boys:
        return "Список юношей пустой"
    elif not girls:
        return "Список девушек пустой"
    
    elif len(boys) != len(girls):
        return "Внимание кто-то может остаться без пары!"
    
    boys_sort = sorted(boys)
    girls_sort = sorted(girls)

    pairs = []
    for i in range(len(boys_sort)):
        pairs.append(f"{boys_sort[i]} и {girls_sort[i]}")

    return pairs 


def input_names(gender):
    names = []
    print(f"\nВведите имена {gender}:")

    count = 1
    while True:
        name = input(f"Имя {count} (Enter для завершения): ").strip()

        if not name:
            if count == 1:
                print("Нужно ввести хотя бы одно имя !")
                continue
            else:
                break

        names.append(name)
        count +=1


    return names


#готовые списки
def show_ready_lists():
    lists = {
        "1": {
            "name": "Классический набор",
            "boys": ['Peter', 'Alex', 'John', 'Arthur', 'Richard'],
            "girls": ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
        },
        "2": {
            "name": "Популярные имена",
            "boys": ['Michael', 'James', 'Robert', 'David', 'William'],
            "girls": ['Sarah', 'Emily', 'Olivia', 'Sophia', 'Jessica']
        },
        "3": {
            "name": "Русские имена",
            "boys": ['Алексей', 'Дмитрий', 'Сергей', 'Андрей', 'Иван'],
            "girls": ['Анна', 'Мария', 'Екатерина', 'Ольга', 'Наталья']
        },
        "4": {
            "name": "Неравные списки (для теста ошибки)",
            "boys": ['Tom', 'Jerry', 'Spike'],
            "girls": ['Tina', 'Lucy']
        },
        "5": {
            "name": "Короткие списки",
            "boys": ['Max', 'Leo'],
            "girls": ['Mia', 'Zoe']
        }
    }

    print("\n" + "Доступные готовые списки" + "="*20)
    for key, value in lists.items():
        print(f"{key}. {value['name']}")
        print(f"   Юноши: {', '.join(value['boys'])}")
        print(f"   Девушки: {', '.join(value['girls'])}")
        print()


    return lists    
        


#тестирую
while True:
    print("\n" + "="*50)
    print("1 Использовать готовые списки")
    print("2 Ввести списки вручную") 
    print("3 Выйти")
    print("="*50)

    choice = input("Ваш выбор: ").strip()

    if choice =="1":
        ready_lists = show_ready_lists()

        while True:
            list_choice = input("\nВыберите номер списка (1-5) или 'back' для возврата: ").strip()

            if list_choice.lower() == 'back':
                break
            elif list_choice in ready_lists:
                selected = ready_lists[list_choice]
                boys = selected['boys']
                girls = selected['girls']
                
                print(f"\nВыбран список: {selected['name']}")
                print(f"Юноши: {', '.join(boys)}")
                print(f"Девушки: {', '.join(girls)}")


                print("\n" + "РЕЗУЛЬТАТЫ " + "="*20)
                result = find_perfect(boys, girls)

                if isinstance(result, list):
                    print("Идеальные пары:")
                    for pair in result:
                        print(f" {pair}")
                else:
                    print(f"! {result}")
                print("="*40)
                break
            else:
                print("Неверный выбор, попробуйте снова")

    elif choice == "2":
        print("\n--- Ввод списка юношей ---")
        boys = input_names("юношей")
        print("\n--- Ввод списка девушек ---")
        girls = input_names("девушек")

        print("\n" + "РЕЗУЛЬТАТЫ " + "="*20)
        result = find_perfect(boys, girls)

        if isinstance(result, list):
            print("Идеальные пары:")
            for pair in result:
                print(f" {pair}")
        else:
            print(f"! {result}")
        print("="*40)
        break
    
    elif choice == "3":
        print("\nДо свидания!")
        break

    else:
        print("Неверный выбор, попробуйте 1, 2 или 3")

