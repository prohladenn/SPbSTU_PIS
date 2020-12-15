my_name = "Валерий"  # Ковшов
task_number = len(my_name) % 4 + 1
print("Вариант: ", task_number)

"""4. Создайте приложение, которое проверяет правильность номера введенной кредитной карты (см.
алгоритм Луна)

Варианты входных данных: 
- Валидная строка - "4561 2612 1234 5467" 
- Невалидная строка по наполнению - "4561 2612 1234 5464"
- Невалидная строка по размеру -  "4561 2612 1234 546" """

# ВВЕДИТЕ СВОЮ СТРОКУ В ЭТУ ПЕРЕМЕННУЮ
input_str = ""  # <- ВОТ СЮДА

input_after_validate = "".join(char for char in input_str if char.isdigit())
if len(input_after_validate) != 16:
    print("Валидация не пройдена")
else:
    sum = 0
    for i in range(0, len(input_after_validate)):
        tmp = int(input_after_validate[i])
        if i % 2 == 0:
            tmp *= 2
            if tmp > 9:
                sum += tmp // 10 + tmp % 10
            else:
                sum += tmp
        else:
            sum += tmp
    if sum % 10 == 0:
        print("Валидация пройдена")
    else:
        print("Валидация не пройдена")
