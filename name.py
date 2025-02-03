import ast


def FamilyName():
    name = input("Enter Your Name : ")
    print(f"Hello , {name}")
def summary(num1 = 0,num2 = 0):
    try:
        # تبدیل ورودی‌ها به عدد صحیح
        num1 =int(input("Enter Your Number1 : "))
        num2 =int(input("Enter Your Number2 : "))
        print(num1 + num2)
    except ValueError:
        print("Check Your Number")
def tedad(tedad = 1):
    try:
        # تبدیل ورودی‌ها به عدد صحیح
        tedad =int(input("Enter Your tedad : "))
        sum = 0
        for _ in range(1,tedad + 1):
            number = int(input(f"Enter Your Number {_} : "))
            sum += number
        print(sum)
    except ValueError:
        print("Check Your Number")


def multiply():
    my_list = []
    try:
        for _ in range(0,int(input("Enter Your Number : "))):
            res = round(float(input(f"Enter Your Number : ")),2)
            my_list.append(res)
        my_list.sort()
    except ValueError:
        return "Check Your Number"
    return my_list
# try:
#     # my_list = input("Enter Your List (example[1,5,3,9]) : ")
#     # my_list = ast.literal_eval(my_list)
#     my_list = input("Enter Your List : ").split(',')
#     print(my_list)
#     find_number = int(input("Enter Your Number : "))
#     if find_number in my_list:
#         print('yes')
#     else :print('No')
# except ValueError:
#     print ("Check Your Number!!!!")

# try:
#     my_list = list(map(int, input("Enter Your List (comma separated, example: 1,5,3,9) : ").split(',')))
#     print(type(my_list))
#     find_number = int(input("Enter Your Number : "))
#
#     print("Yes" if find_number in my_list else "No")
#
# except ValueError:
#     print("Check your input! Make sure you enter valid numbers.")
#
# try:
#     list_odd = []
#     my_list = list(map(int, input("Enter Your List (comma separated, example: 1,5,3,9) : ").split(',')))
#     for i in my_list:
#         if i % 2 == 0:
#             list_odd.append(i)
#     list_odd.sort()
#     print(list_odd)
# except ValueError:
#     print("Check your input! Make sure you enter valid numbers.")
# try:
#     my_list = list(map(int, input("Enter Your List (comma separated, example: 1,5,3,9) : ").split(',')))
#     list_even = sorted([num for num in my_list if num % 2 == 0])  # فیلتر و مرتب‌سازی همزمان
#     print(list_even)
# except ValueError:
#     print("Check your input! Make sure you enter valid numbers.")

# print(multiply())

# def divide():
#     numbers = input("Enter Your Number and use , to divide : ")
#     numbers = [round(float(num), 2) for num in numbers.split(",")]
#     numbers.sort()
#     return numbers
# print(divide())





# number =int(input("Enter Your number : "))
# factor = 1
# for i in range(1,number + 1):
#     factor *= i
# print(factor)
# import math
# try:
#     number = int(input("Enter Your number : "))
#     print(math.factorial(number))
# except ValueError:
#     print("Check your input! Make sure you enter valid numbers.")


# my_text = input("Enter your text :")
# num = 0
# for char in my_text:
#     if char == 'a':
#         num += 1
# print(num)
# my_text = input("Enter your text : ")
# num = my_text.count('a')  # استفاده از count برای شمارش تعداد 'a'
# print(num)

try:
    # my_list = list(map(int, input("Enter Your List (comma separated, example: 1,5,3,9) : ").split(',')))
    # print(my_list[::-1])
    my_list = list(map(int, input("Enter Your List (comma separated, example: 1,5,3,9) : ").split(',')))
    print(list(reversed(my_list)))
except ValueError:
    print('aaa')