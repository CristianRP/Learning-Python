from datetime import date, timedelta

def all_saturdays(year):
    count = 0
    # 1ero de Enero del año en curso
    dt = date(year, 1, 1)
    # Primer sabado del año
    dt += timedelta(days=12 - dt.weekday())
    while dt.year == year:
        yield dt
        dt += timedelta(days=7)
        count += 1
    print('Total de Sábados: {0}'.format(count))

for s in all_saturdays(2017):
    print(s)