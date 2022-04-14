year=input('Введите год: ')
ys1=int(year) % 4
ys2=int(year) % 100
ys3=int(year) % 400
if ys3 == 0 or (ys1 ==0 and ys2 !=0):
    print('Год високосный.')
else:
    print('Год не високосный')

