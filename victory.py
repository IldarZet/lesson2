while True:
    right = 0
    error = 0

    year = int(input('Input Till Lindemann born year: '))

    if year == 1963:
        right += 1
    else:
        print('Правильный ответ 1963')
        error += 1

    year = int(input('Input Marilyn Manson born year: '))

    if year == 1969:
        right += 1
    else:
        print('Правильный ответ 1969')
        error += 1

    year = int(input('Input Ozzy Osbourne born year: '))

    if year == 1948:
        right += 1
    else:
        print('Правильный ответ 1948')
        error += 1

    year = int(input('Input James Alan Hetfield born year: '))

    if year == 1963:
        right += 1
    else:
        print('Правильный ответ 1963')
        error += 1

    year = int(input('Input Amy Lynn Hartzler born year: '))

    if year == 1981:
        right += 1
    else:
        print('Правильный ответ 1981')
        error += 1

    print('Правильные ответы - ' + str(right))
    print('Ошибки - ' + str(error))
    print('% Правильных ответов - ' + str(right*100/5) + '%')
    print('% Ошибок - ' + str(error*100/5) + '%')

    answer = input('Хотите сыграть еще? (Да/Нет): ')
    if answer == 'Нет':
        break
    else:
        continue