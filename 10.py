a=input('Введите число: ')
b=input('Введите число: ')
c=input('Введите число: ')
if int(a)>int(b) and int(a)>int(c):
    print(a)
    if int(b)>int(c):
        print(c)
        print(b)
    else:
        print(b)
        print(c)
if int(b)>int(a) and int(b)>int(c):
    print(b)
    if int(a)>int(c):
        print(c)
        print(a)
    else:
        print(a)
        print(c)
if int(c)>int(a) and int(c)>int(b):
    print(c)
    if int(a)>int(b):
        print(b)
        print(a)
    else:
        print(a)
        print(b)


        
