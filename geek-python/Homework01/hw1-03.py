# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3
number = int(input("Введите число >>>"))
str_number = str(number)
str_numt1 = str_number + str_number
str_num2 = str_number + str_number + str_number
glue = number + int(str_numt1) + int(str_num2)
print("Результат равен:", glue)