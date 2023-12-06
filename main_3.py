try:
    matrix = []
    n = int(input("Введите количество строк матрицы: "))
    m = int(input("Введите количество столбцов матрицы: "))
    column_sums = [0] * m

    for i in range(n):
        row = [0] * m
        matrix.append(row)

    for i in range(n):
        for j in range(m):
            matrix[i][j] = int(input(f"Введите элемент матрицы ({i + 1}, {j + 1}): "))
    for i in matrix:
        print(i)
    for j in range(m):
        for i in range(n):
            if matrix[i][j] < 0:
                break
        else:
            column_sums[j] = sum(matrix[i][j] for i in range(n))
    for i in range(m):
        if column_sums[i] > 0:
            print(f"Сумма элементов в столбце {i + 1} = {column_sums[i]}")
except ValueError:
    print("Введенное значение не является натуральным числом.")

