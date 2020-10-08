# def check_fermat(a, b, c, n):
#     if n > 2 and (a ** n + b ** n == c ** n):
#         print("Holy smokes, Fermat was wrong!")
#     else:
#         print("No, that doesn't work.")
#
#
# def check_numbers():
#     a = int(input("Choose a number for a: "))
#     b = int(input("Choose a number for b: "))
#     c = int(input("Choose a number for c: "))
#     n = int(input("Choose a number for n: "))
#     return check_fermat(a, b, c, n)
#
#
# check_numbers()
#
#
# my_colors = ["red", "orange", "blue", "yellow"]
#
# for i in range(0, len(my_colors)):
#     print(my_colors[i])
#
# some_colors = my_colors[1:]
# print(some_colors)
#
# new_colors = [c[0:5] for c in my_colors if len(c) < 5]
# print(new_colors)
#
# my_animals = ("dog", "cat", "fish")  # tuple
#
# my_cities = {"Dallas", "spokane", "seattle"}
#
# my_cities.add("reardan")
# print(my_cities)
# my_cities.update(["bourne", "travistown"])
# print(my_cities)  # .pop .remove
# print(len(my_cities))
#
# english_spanish =  {"one": "uno", "two": "dos", "three": "tres", "four": "cuatro", "five": "cinco", "six": "seis", "seven": "seite", "eight": "ocho", "nine": "nueve", "ten": "diez"}
#
#
# print(english_spanish["five"])

# def print_nums(start_int, length_int):
#     for it in range(start_int, length_int + 1):
#         print(it)
#
#
# print_nums(1, 10)
#
# for items in range(10, 0, -1):
#     print(items)
#
# numbers_list = [22, 55, 34, 23, 2]
#
# for i in range(len(numbers_list)):
#     print(f"Hello!, {i}: {numbers_list[i]}")
#
# for num in enumerate(numbers_list):
#     print(f"Hello!, {num}")
#
# for t in enumerate(numbers_list):
#     i = t[0]
#     v = t[1]
#     print(f"{i}: {v}")
#
# for i, v in enumerate(numbers_list):
#     print(f"{i}: {v}")

def digitsManipulations(n):
    total = 0
    product = 1
    while (n != 0):
        product = product * (int(n % 10))
        total = total + int(n % 10)
        n = int(n // 10)
        print(n)
    #
    # while (m != 0):
    #
    #     m = int(m // 10)
    #     print(m)
    final = product - total
    return final

print(digitsManipulations(1000344))
