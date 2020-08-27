#dz5-3

with open('dz5-3.txt', 'r') as my_file:
    data_1 = []
    data_2 = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           data_2.append(i[0])
        data_1.append(i[1])
print(f'Оклад меньше 20.000 {data_2}, средний оклад {sum(map(int, data_1)) / len(data_1)}')