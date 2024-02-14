russian_alph = 'ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮёйцукенгшщзхъфывапролджэячсмитьбю'


def contains_from_alph(seq: str, alph: str) -> bool:
    """Простая функция проверки, содержится ли какой либо символ из
    алфавита в данной последовательности

    :param seq: Входная строка (последовательность), в которой нужно найти любой символ из алфавита
    :param alph: Алфавит
    :return: Булевое значение - True, если какой-нибудь символ из алфавита есть в строке
    """
    for c in alph:
        if c in seq:
            return True
    return False


russian_artists = []
foreign_artists = []

with open('songs.csv', 'r', encoding='UTF-8') as r:
    with open('russian_artists.txt', 'w', encoding='UTF-8') as rw:
        with open('foreign_artists.txt', 'w', encoding='UTF-8') as fw:
            artists = set(map(
                lambda line: line.removesuffix('\n').split(';')[1],
                r.readlines()
            ))

            for artist in artists:
                # В списке встречаются исполнители без имени,
                # а точнее с подписью unknown. В лучшем случае
                # для точной проверки их либо пропускать, либо
                # анализировать другим способом, но так как
                # в задании об этом нет речи, код для пропуска
                # закомментирвоан:
                #
                # if artist == 'unknown':
                #     continue
                if contains_from_alph(artist, russian_alph):
                    russian_artists.append(artist)
                else:
                    foreign_artists.append(artist)

            rw.write('\n'.join(russian_artists))
            fw.write('\n'.join(foreign_artists))

print(f'Количество российских исполнителей: {len(russian_artists)}')
print(f'Количество иностранных исполнителей: {len(foreign_artists)}')
