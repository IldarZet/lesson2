year = int(input('Input Pushkin born year: '))

if year == 1799:
    print('Верно')
    birthday = int(input('Input Pushkin birthday: '))
    if birthday == 26:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверый год рождения')

print('End')