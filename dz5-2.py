#dz5-2

my_file = open('dz5-2.txt', 'r')
content = my_file.read()
print(f'Сам файл: \n {content}')
my_file = open('dz5-2.txt', 'r')
content = my_file.readlines()
print(f'Количество строк - {len(content)}')
my_file = open('dz5-2.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} - (ой) строки {len(content[i])}')
my_file = open('dz5-2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()