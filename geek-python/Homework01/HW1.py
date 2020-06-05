# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

#
# m = 5
# a = 10
# print(m)
# print(a)

# zagadka01 = ("В Полотняной стране По реке Простыне Плывет пароход То назад, то вперед, А за ним такая гладь — Ни морщинки не видать.")
# answer01 = input("Введите ответ загадки >>>")
#
# good_answer01 = "утюг"
#
# if good_answer01 == answer01:
#     print("Верно")
# else:
#     print("Неверно")


# number = int(input("Введите число >>>"))
# print("Вы ввели", number)


#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.


# second_time = int(input("Введите время в секундах >>>"))
# h = str(second_time // 3600)
# m = (second_time // 60) % 60
# s = second_time % 60
# if m < 10:
#     m = '0'+str(m)
# else:
#     m = str (m)
# if s < 10:
#     s = '0'+str(s)
# else:
#     s = str(s)
# print(h+':'+m+':'+s)

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3
# number = int(input("Введите число >>>"))
# str_number = str(number)
# str_numt1 = str_number + str_number
# str_num2 = str_number + str_number + str_number
# glue = number + int(str_numt1) + int(str_num2)
# print("Результат равен:", glue)

#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
str_number = input("Введите положительное число >>>")
i = len(str_number)
print("Длина строки равна: ", i)
#print(str_number[0])
#print(str_number[1])
#print(str_number[2])


number = 0
max_digit = 0
for number in range(i):
    print("number = ",number, " str_number[", number,"] = " , str_number[number]);
    if (max_digit < ord(str_number[number])):
            max_digit = ord(str_number[number])
    print("Максимальная цифра в строке = ", chr(max_digit))

# current_count = 0
#
# while
#     if curre  nt_count == i:
#         break
#
# current_count += 1
#
#     if current_count == i:
#         continue
#
# print(str_number[current_count])






























