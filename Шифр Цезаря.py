# Английский загл по Unicode 65 - 90

# Английский строчный по Unicode 97 - 122


# Русский загл по Unicode 1040 - 1071


# Русский строчные по Unicode 1072 - 1103

def shifr_ru():  # Шифруем русский
    print("Введите текст на русском языке:")
    txt = input()
    for step in range(1, 33):
        print(step, end='. ')
        if step > 32:
            step = step % 32
        for i in txt:
            if i == ' ' or i == ',' or i == "!" or i == '.' or i == '?' or i == ':' or i == '(' or i == ')':
                print(i, end='')
            else:
                n = ord(i) + step
                if 1071 < n < 1071 + step + 1:
                    n = 1039 + (n - 1071)
                elif n > 1103:
                    n = 1071 + (n - 1103)
                print(chr(n), end='')
        print()


def deshifr_ru():  # Дешифруем русский
    print("Введите текст на русском языке:")
    txt = input()
    for step in range(1, 33):
        print(step, end='. ')
        if step > 32:
            step = step % 32
        for i in txt:
            if i == ' ' or i == ',' or i == "!" or i == '.' or i == '?' or i == ':' or i == '(' or i == ')':
                print(i, end='')
            else:
                n = ord(i) - step
                if 1040 > n:
                    n = 1072 - (1040 - n)
                elif 1072 - step - 1 < n < 1072:
                    n = 1104 - (1072 - n)
                print(chr(n), end='')
        print()


def shifr_eng():  # Шифруем английский
    print("Введите текст на английском языке:")
    txt = input()
    for step in range(1, 27):
        print(step, end='. ')
        if step > 27:
            step = step % 27
        for i in txt:
            if i == ' ' or i == ',' or i == "!" or i == '.' or i == '?' or i == ':' or i == '(' or i == ')':
                print(i, end='')
            else:
                n = ord(i) + step
                if 90 < n < 90 + step:
                    n = 64 + (n - 90)
                elif n > 122:
                    n = 96 + (n - 122)
                print(chr(n), end='')
        print()


def deshifr_eng():  # Дешифруем английский
    print("Введите текст на английском языке:")
    txt = input()
    for step in range(1, 27):
        print(step, end='. ')
        if step > 27:
            step = step % 27
        for i in txt:
            if i == ' ' or i == ',' or i == "!" or i == '.' or i == '?' or i == ':' or i == '(' or i == ')':
                print(i, end='')
            else:
                n = ord(i) - step
                if n < 65:
                    n = 91 - (65 - n)
                elif 97 - step - 1 < n < 97:
                    n = 123 - (97 - n)
                print(chr(n), end='')
        print()


def start():
    print('Выберите язык ввода: 1 - русский, 2 - английский.')
    ans1 = int(input())
    print('Шифруем или дешифруем? 1 - шифруем, 2 - дешифруем.')
    ans2 = int(input())
    if ans1 == 1:
        if ans2 == 1:
            shifr_ru()
        elif ans2 == 2:
            deshifr_ru()
    elif ans1 == 2:
        if ans2 == 1:
            shifr_eng()
        elif ans2 == 2:
            deshifr_eng()


def Ave_Cesar():
    from string import punctuation
    text = input().split()
    s = []
    for i in text:
        step = len(i.strip(punctuation))
        if step > 27:
            step = step % 27
        new_i = ''
        for j in i:
            if j not in punctuation:
                n = ord(j) + step
                if 90 < n < 90 + step:
                    n = 64 + (n - 90)
                elif n > 122:
                    n = 96 + (n - 122)
                j = chr(n)
                new_i += j
            if j in punctuation:
                new_i += j
        print(new_i, end=' ')

start()