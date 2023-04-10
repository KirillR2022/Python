

def view_FB():
    with open('Fone_book.txt', 'r', encoding='UTF-8') as f:
        for i in list(enumerate(f)):
            print(f'{int(i[0]) + 1}. {i[1]}')


def create_cont():
    a = input("Введите ФИО через точу с запятой(;):  ")

    with open('Fone_book.txt', 'a', encoding='UTF-8') as f:
        f.write('\n')
        f.write(a)


def delete_cont():
    with open('Fone_book.txt', 'r', encoding='UTF-8') as f:
        arr = list(enumerate(f))
        for i in arr:
            print(f'{int(i[0]) + 1}. {i[1]}')
    del_num = int(input("Введите номер который Вы хотите удалить: "))
    with open('Fone_book.txt', 'w', encoding='UTF-8') as f1:
        for a in arr:
            if del_num != int(a[0]) + 1:
                f1.write(a[1])


while True:
    print('1)  Контакты')
    print('2)  Создать контакт')
    print('3)  Удалить контакт')
    print('4)  Выход')
    n = int(input('Введите номер интересующей Вас строки:  '))
    if n == 1:
        view_FB()
    if n == 2:
        create_cont()
    if n == 3:
        delete_cont()
    if n == 4:
        break


