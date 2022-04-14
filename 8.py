x = input('Введите первое число: ')
y = input('Введите второе число: ')
zn = input('Введите знак (+, -, /, *, mod, pow, div): ')
if zn == '+':
    print(float(x)+float(y))
elif zn == '-':
    print(float(x)-float(y))
elif zn == '/':
    if float(y) != 0:
        print(float(x)/float(y))
    else:
        print('Деление на 0!')
elif zn == '*':
    print(float(x)*float(y))
elif zn == 'mod':
    print(float(x)%float(y))
elif zn == 'pow':
    print(float(x)**float(y))
elif zn == 'div':
    print(float(x)//float(y))
else:
    print('Неверный знак!')
    
