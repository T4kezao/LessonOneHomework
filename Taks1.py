a = int(input('Введите день недели:'))
if a>=1 and a<=5:
    print('Это будний день!')
elif a<=0:
    print('Некорректное значение! Попробуйте снова!')    
else:
    print('Это выходной!')