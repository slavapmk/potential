with open('songs.csv', 'r', encoding='UTF-8') as fr:
    lines = list(map(
        lambda line: line.removesuffix('\n').split(';'),
        fr.readlines()
    ))
    names = list(map(
        lambda line: line[1],
        lines
    ))
    while True:
        name = input('Введите имя артиста: ')
        if name == '0':
            exit()
        try:
            row = lines[names.index(name)]
            print(f'У {name} найдена песня: {row[2]}')
        except ValueError:
            print('К сожалению, ничего не удалось найти')
