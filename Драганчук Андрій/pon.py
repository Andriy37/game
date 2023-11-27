notes = {}  # словник для зберігання записів

def add_note():
    title = input("Введіть заголовок запису: ")
    content = input("Введіть вміст запису: ")
    notes[title] = content
    print("Запис успішно додано!")

def view_notes():
    if not notes:
        print("У вас немає жодного запису.")
    else:
        print("Ваші записи:")
        for title, content in notes.items():
            print(f"Заголовок: {title}\nВміст: {content}\n")

def delete_note():
    if not notes:
        print("Немає записів для видалення.")
    else:
        title_to_delete = input("Введіть заголовок запису для видалення: ")
        if title_to_delete in notes:
            del notes[title_to_delete]
            print(f"Запис '{title_to_delete}' успішно видалено!")
        else:
            print(f"Запис з заголовком '{title_to_delete}' не знайдено.")

def main():
    while True:
        print("\nМеню:")
        print("1. Додати запис")
        print("2. Переглянути всі записи")
        print("3. Видалити запис")
        print("4. Вийти з програми")
        
        choice = input("Виберіть опцію (1/2/3/4): ")

        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Будь ласка, виберіть знову.")

if __name__ == "__main__":
    main()

