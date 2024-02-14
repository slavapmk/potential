popularity: dict[str, int] = {}


def increment(key) -> None:
    """Простая функция для инкрементирования или инициализации значение по ключу внутри словаря, описанного выше

    :param key: Ключ для инкрементирования в словаре
    """
    global popularity
    popularity[key] = popularity.get(key, 0) + 1


with open('songs.csv', 'r', encoding='UTF-8') as r:
    lines = list(map(
        lambda line: line.removesuffix('\n').split(';'),
        r.readlines()
    ))
    tracks = list(map(
        lambda line: line[2],
        lines
    ))

    for row_id, row in enumerate(lines):
        if tracks.index(row[2]) < row_id:
            increment(lines[tracks.index(row[2])][1])
        else:
            increment(row[1])

# Для сбора статистики удобно было бы отсортировать таблицу по
# количеству прослушиваний, но в задании не было указано это
for line_id, key in enumerate(popularity):
    if line_id >= 10:
        break
    print(f'{key} выпустил {popularity[key]} песен.')
