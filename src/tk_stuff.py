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


my_colors = ["red", "orange", "blue", "yellow"]

for i in range(0, len(my_colors)):
    print(my_colors[i])

some_colors = my_colors[1:]
print(some_colors)

new_colors = [c[0:5] for c in my_colors if len(c) < 5]
print(new_colors)

my_animals = ("dog", "cat", "fish")  # tuple

my_cities = {"Dallas", "spokane", "seattle"}

my_cities.add("reardan")
print(my_cities)
my_cities.update(["bourne", "travistown"])
print(my_cities)  # .pop .remove
print(len(my_cities))

english_spanish =  {"one": "uno", "two": "dos", "three": "tres", "four": "cuatro", "five": "cinco", "six": "seis", "seven": "seite", "eight": "ocho", "nine": "nueve", "ten": "diez"}


print(english_spanish["five"])

