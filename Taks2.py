# Задание 2 часть 2.

x = int(input('Введите координату x: '))
y = int(input('Введите координату y: '))
if x>0 and y>0:
    print('Точка находится в 1 четверти')
if x<0 and y>0:
    print('Точка находится в 2 четверти')
if x>0 and y<0:
    print('Точка находится в 4 четверти')
if x<0 and y<0:
    print('Точка находится в 3 четверти')
if x==0 and y==0:
    print('Некорректные значения! Координаты не могут быть равны 0!')      
