#dz5-7

import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('dz5-7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Средняя прибыль - {prof_aver:.2f}')
    else:
        print(f'Убыток')
    pr = {'Средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('dz5-7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Файл json: \n '
          f' {js_str}')