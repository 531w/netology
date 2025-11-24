documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]


directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}

def find_owner_document(doc_number): #Поиск владельца документа по номеру 
    for doc in documents:
        if doc['number'] == doc_number:
            return doc['name']
    return None
def main():
    while True:
        command = input("\nВведите команду: ").strip().lower()

        if command == 'q':
            print("Выход из программы.")
            break

        elif command == 'n':
            doc_number = input("Введите номер документа: ").strip()
            owner = find_owner_document(doc_number)

            if owner:
                print(f"Владелец документа: {owner}")
            else:
                print("Документ с таким номером не найден")

        else:
            print("Неизвестна команда, доступные команды: n, q")

if __name__ == "__main__":
    main()