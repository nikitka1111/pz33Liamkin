import math
fig=input('Введите фигуру (Треугольник, Прямоугольник, Круг): ')
if fig == 'Треугольник':
    a=input('Введите длину стороны 1: ')
    b=input('Введите длину стороны 2: ')
    c=input('Введите длину стороны 3: ')
    p=(float(a)+float(b)+float(c))/2
    print('Площадь: ', math.sqrt(float(p)*(float(p)-float(a))*(float(p)-float(b))*(float(p)-float(c))))
elif fig == 'Прямоугольник':
    a=input('Введите длину стороны 1: ')
    b=input('Введите длину стороны 2: ')
    print('Площадь: ', float(a)*float(b))
elif fig == 'Круг':
    r=input('Введите радиус: ')
    print('Площадь: ', 3.14*float(r)**2)
else:
    print('Неверно введена фигура!')
