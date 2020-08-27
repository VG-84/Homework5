#dz5-5

def summary():
    try:
        with open('dz5-5.txt', 'w+') as file_obj:
            line = input('Введите цифры\n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка')
    except ValueError:
        print('Номер неверный')
summary()