number = int(input("Enter Your Number : "))
for division in range(2,number + 1):
    is_prime = True
    for check in range(2,int(division ** 0.5)+1):
        if division % check == 0:
            is_prime = False
            break
    if is_prime:
        print(division)
