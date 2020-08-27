#dz5-1

import os

file_path = os.path.join(os.path.dirname(__file__), 'dz5-1.txt')
with open(file_path, 'w', encoding='UTF-8') as file:
    while True:
        user_data = input('Ввод данных\n')
        if not user_data:
            break
        file.write(f'{user_data}\n')