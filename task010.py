"""Задача 10
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
Пример:
5 -> 1 0 1 1 0
2"""

from random import randint
coin_num = int(input("Введите количество монеток: "))
tails, emblem = 0, 0
for _ in range(coin_num):
    side_coin = randint(0, 1)
    print(side_coin, end=' ')
    if side_coin == 1:
        tails += 1
    else:
        emblem += 1
print()
if tails == 0 or emblem == 0:
    print('Монеты не нужно переворачивать')
elif tails > emblem:
    print(f'Необходимо перевернуть {emblem} c гербом')
elif tails == emblem:
    print(f'Можно перевернуть любые монеты, монет с решкой = {tails}, монет с гербом = {emblem}')
else:
    print(f'Необходимо перевернуть {tails} c решкой')
