"""
    db format: {
        idx: {
            'name': str,
            'desc': str,
        }
    }
"""

import json


def read_db() -> dict:
    try:
        with open('database.json', 'r', encoding='utf-8') as db:
            data = json.load(db)

        return data
    except json.decoder.JSONDecodeError:
        return {}


def create_db(name: str, desc: str) -> int:
    data = read_db()

    try:
        last_key = list(data.keys())[-1]
        new_key = int(last_key) + 1
    except IndexError:
        new_key = 1

    data[f'{new_key}'] = {'name': name, 'desc': desc}

    with open('database.json', 'w', encoding='utf-8') as db:
        json.dump(data, db, ensure_ascii=False, indent=4)

    return 200


def update_db(
        idx: str,
        new_name: str,
        new_desc: str
):
    data = read_db()
    data[idx] = {'name': new_name, 'desc': new_desc}

    with open('database.json', 'w', encoding='utf-8') as db:
        json.dump(data, db, ensure_ascii=False, indent=4)

    return 200


def delete_db(
        idx: str
):
    data = read_db()

    if idx in data:
        data.pop(idx)
        with open('database.json', 'r+', encoding='utf-8') as db:
                        json.dump(data, db, ensure_ascii=False, indent=4)
        print(f'Заметка успешно удалена!')
        print(' ')


if __name__ == '__main__':
    # print(read_db())
    # create_db('new note 2', 'new desc 2')
    update_db('1', 'new note', 'new desc')