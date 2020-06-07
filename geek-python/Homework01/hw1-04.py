#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
str_number = input("Введите положительное число >>>")
i = len(str_number)
print("Длина строки равна: ", i)

max_digit = 0
ind = 0
while ind < i:
    # print("Позиция цифры в строке = ",ind + 1, " цифра в строке  -> " , str_number[ind]);
    if (max_digit < ord(str_number[ind])):
            max_digit = ord(str_number[ind])
    ind += 1

print("Максимальная цифра в строке = ", chr(max_digit))