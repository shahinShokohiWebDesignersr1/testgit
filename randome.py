number = int(input('Enter your number : '))
if number < 2 :
    print("No")
elif number == 2 :
    print("Yes")
elif number % 2 == 0 :
    print("No")
else :
    is_prime = True
    for prime in range(3,int(number ** 0.5)+1,2):
        if number % prime == 0:
            is_prime = False
            break
    print("Yse" if is_prime else "No")
# test