from crud import create_db, read_db


def create_note():
    name = input('Введите имя заметки: ')
    desc = input('Введите описание заметки: ')

    status_code = create_db(name=name, desc=desc)
    if status_code == 200:
        print('Заметка успешно создана\n')
    else:
        print('Ошибка! Попробуйте еще раз!\n')


def read_all_notes():
    notes = read_db()

    if notes:
        print('Ваши актуальные заметки:')
        for key, value in notes.items():
            print(f'{key}. {value["name"]}: {value["desc"]}')
        print(' ')
    else:
        print('Заметок пока что нет...')
        print(' ')


def update_note():
    pass


def delete_note():
    pass


def main():
    while True:
        operation = input(
            f'1 - Посмотреть заметки\n'
            f'2 - Создать заметку\n'
            f'3 - Обновить заметку\n'
            f'4 - Удалить заметку\n'
            f'! - Для выхода из программы\n'
            f'Введите цифру операции: '
        )
        print(' ')

        match operation:
            case '1':
                read_all_notes()
            case '2':
                create_note()
            case '!': break


if __name__ == '__main__':
    main()
