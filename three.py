# Задача 6

n = input('Введите шестизначный номер вашего билета: ')
if len(n) == 6:
    if sum(map(int, n[:3])) == sum(map(int, n[3:])):
            print('Ваш билет счастливый!')
    else:
            print('Ваш билет не счастливый(')
else:
    print('Введен некорректный номер билета')