try:
    x = int(input("Введите значение x: "))
    y = int(input("Введите значение y: "))
    result = x/y
    print(f"Результат деления: {result}")
except ZeroDivisionError:
    print("Деление на ноль!")
except ValueError:
    print("Ошибка преобразования типа данных")
finally:
    print("Программа завершена!")