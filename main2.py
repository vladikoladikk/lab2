import random
def process_argument(arg):
    if isinstance(arg, list):
        sum_of_even = sum(x for x in arg if x % 2 == 0)
        arg = [x for x in arg if x != 0]
        return sum_of_even, arg
    elif isinstance(arg, set):
        max_element = max(arg)
        arg.remove(max_element)
        return max_element, arg
    elif isinstance(arg, int):
        is_prime = True
        if arg <= 1:
            is_prime = False
        else:
            for i in range(2, int(arg ** 0.5) + 1):
                if arg % i == 0:
                    is_prime = False
                    break
                return is_prime
    elif isinstance(arg, str):
        most_common_char = max(set(arg), key=arg.count)
        return most_common_char
    else:
         return "Неизвестный тип аргумента"

def fill_set_with_random_numbers(collection, size):
    for _ in range(size):
        random_number = random.randint(-10, 10)
        collection.add(random_number)
def fill_list_with_random_numbers(collection, size):
    for _ in range(size):
        random_number = random.randint(-10, 10)
        collection.append(random_number)

arg_list = []
fill_list_with_random_numbers(arg_list, 10)
result1 = process_argument(arg_list)
print(arg_list)
print("Сумма четных чисел и список без нулей:", result1)

arg_set = set()
fill_set_with_random_numbers(arg_set, 10)
print(arg_set)
result2 = process_argument(arg_set)
print("Максимальный элемент и множество без него:", result2)

arg_number = random.randint(-10, 10)
print(arg_number)
result3 = process_argument(arg_number)
print("Число является простым:", result3)

arg_string = "hello world"
result4 = process_argument(arg_string)
print("Наиболее часто встречающийся символ:", result4)




