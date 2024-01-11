def prime_number(s):
    if (s < 2):
        return False
    for i in range(2, int(s / 2) + 1):
        if (s % i == 0):
            return False
    return True

number = int(input("Sayi girin: "))
if(prime_number(number)):
    print("prime number")
    exit()
print("not prime number")