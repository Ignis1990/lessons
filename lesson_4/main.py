from crud import create_db, read_db, update_db, delete_db


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
    notes = read_db()

    if notes:
        idx = input(f'Введите номер заметки, которую Вы хотите откорректировать: ')
        if idx in notes.keys():
            # for idx in notes.keys():
            new_name = input(f'Введите новое имя заметки: ')
            new_desc = input(f'Введите новое описание заметки: ')
            status_update = update_db(idx=idx, new_name=new_name, new_desc=new_desc)
            if status_update == 200:
                print('Заметка успешно обновлена!\n')
                print(' ')
            else:
                print('Ошибка! Попробуйте еще раз!\n')
                print(' ')
        else:
            print(f'Такой заметки не существует!')
            print(' ')
    else:
        print('Нет заметок для редактирования.')
        print(' ')


def delete_note():
    idx = input(f'Укажите номер заметки, которую вы хотите удалить: ')
    notes = read_db()
    if idx in notes.keys():
        delete_db(idx=idx)
    else:
        print(f'Такой заметки не найдено. Пожалуйста, введите корректный номер заметки.')
        print(' ')
# Не работает!
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
            case '3':
                update_note()
            case '4':
                delete_note()
            case '!': break


if __name__ == '__main__':
    main()
