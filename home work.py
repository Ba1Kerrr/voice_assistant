Full_num = input("введите 3х значное число")
if len(Full_num) == 3:
    Full_num = int(Full_num)
    x = Full_num // 100
    y = Full_num // 10 % 10
    z = Full_num % 10
    Amount_Num = x + y + z
    print(Amount_Num)
elif len(Full_num) < 3:
    print('Это не 3х значное число.Код завершен')
else :
    print('Это не 3х значное число.Код завершен')