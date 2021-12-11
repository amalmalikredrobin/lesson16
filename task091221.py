# def calculator(func, a, b):
#     return func(a, b)
# def add(a, b):
#     return a + b 
# def divide(a, b):
#     return a / b
# def subtract(a, b):
#     return a - b
# def multiply(a, b):
#     return a * b


# print(calculator(add, 2, 3))
# print(calculator(add, 2, 3))
# print(calculator(add, 2, 3))
# print(calculator(add, 2, 3))



# def sum_numbers(txt: str)
#     acc = 0
#     list = txt.split(' ')
#     for word in list:
#         if word.isdigit(): acc += int(word)
#     return acc


def checkio(array):
    # if len(array) == 0:
    #     return 0
    # else:
    #     last = array[len(array)-1]
    #     evens = array[::2]
    #     total = 0
    #     for i in evens:
    #         total = total + i
    #     return total * last
    if len(n) >=1:
        return (sum(n[0::2])) * n[-1]
    else:
        return 0

checkio([0, 1, 2, 3, 4, 5])
