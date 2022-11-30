from time import sleep
from v1.library_1v import library_1

def start():
    t = input('введите: ')
    e = open(library_1[t], 'r', -1, 'utf-8')
    for LINE in e:
        print(LINE, end='')
        sleep(0.5)
    e.close()
    sleep(1)
    print('\n')

    s = []
    e0 = open(library_1[t], 'r', -1, 'utf-8')
    r = e0.readlines()
    r1 = ', '.join(r).split(' ')
    for r1 in r1:
        if r1 in library_1:
            s.append(r1)

    if len(s) == 1:
        print(f'Жмите: {s[0]}')
    elif len(s) == 2:
        print(f'Ваш выбор: {s[0]} или {s[1]}')
    elif len(s) == 3:
        print(f'Ваш выбор: {s[0]}, {s[1]} или {s[2]}')
    elif len(s) == 4:
        print(f'Ваш выбор: {s[0]}, {s[1]}, {s[2]} или {s[3]}')

    e0.close()


def game():
    print('Здравствуй дорогой читатель. По всей видимости ты любитель книг и в душе исследователь всего неведанного и '
          'странного. Эта книга или точнее сказать Книга - игра, изобилует и тем и другим. Не буду раскрывать '
          'всех ее тайн и предлагаю уже перейти к книге самому и убедиться в этом. Могу еще добавить одно ПРИЯТНОЙ '
          'ИГРЫ БУДУЩИЙ КУРСАНТ И ЖМИ на клаве 400!')

    num = 0
    while True:
        num += 1

        start()

game()