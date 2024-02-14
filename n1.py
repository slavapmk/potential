from datetime import datetime, timezone

max_date = datetime(2002, 1, 1, tzinfo=timezone.utc)

with open('songs.csv', 'r', encoding='UTF-8') as fr:
    with open('songs_new.csv', 'w', encoding='UTF-8') as fw:
        lines = list(map(
            lambda line: line.removesuffix('\n').split(';'),
            fr.readlines()
        ))

        for row_id, row in enumerate(lines):
            if row_id > 0:
                date: str = row[3]
                split = list(map(int, date.split('.')))
                day, month, year = split[0], split[1], split[2]

                datet = datetime(year, month, day, tzinfo=timezone.utc)

                if datet < max_date:
                    print(f"{row[2]} - {row[1]} - {row[0]}")

                if int(row[0]) == 0:
                    row[0] = round(abs(
                        (max_date - datet).days / (len(row[1]) + len(row[2]))
                    ) * 10000)
            fw.write(';'.join(map(str, row)) + '\n')
