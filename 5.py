x=input('Введите количество минут для сна: ')
h=input('Введите во сколько часов вы засыпаете: ')
m=input('Введите во сколько минут вы засыпаете: ')
h=int(h) * 60
x=int(x) + int(h) + int(m)
chas = int(x) // 60
minute = int(x) % 60 
print(chas)
print(minute)
