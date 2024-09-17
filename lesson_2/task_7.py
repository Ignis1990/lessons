phrase = input('Фраза: ')

phrase_list = phrase.split(' ')
for i in range(len(phrase_list)):
    word = phrase_list[i]

    if len(word) > 10:
        word = f'{word[:10]}...'
    print(f'{i + 1}. {word}')


# k = '123456789'
# print(k[:5])