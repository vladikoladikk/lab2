def sum(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Деление на ноль")
    return x / y


while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("0. Выход")

    choice = input("Введите номер операции: ")

    if choice == '0':
        break

    if choice not in ['1', '2', '3', '4']:
        print("Неверный ввод. Пожалуйста, выберите снова.")
        continue

    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Неверный формат числа. Пожалуйста, введите числа снова.")
        continue

    if choice == '1':
        result = sum(num1, num2)
        print("Результат:", result)
    elif choice == '2':
        result = subtract(num1, num2)
        print("Результат:", result)
    elif choice == '3':
        result = multiply(num1, num2)
        print("Результат:", result)
    elif choice == '4':
        try:
            result = divide(num1, num2)
            print("Результат:", result)
        except ZeroDivisionError as zeroDivision:
            print("Ошибка:", zeroDivision)

print("Программа завершена.")
