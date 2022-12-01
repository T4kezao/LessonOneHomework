import math

x1 = float(input('Введите координату x первой точки: '))
y1 = float(input('Введите координату y первой точки: '))
x2 = float(input('Введите координату x второй точки: '))
y2 = float(input('Введите координату y второй точки: '))

distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
print('Расстояние между точкой 1 и точкой 2 =' , distance)