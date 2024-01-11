import random

def perm_number(random_num, num):
    perm = 0

    num_ = set(str(num))
    _new = list(num_)
    for eleman in _new:
        tekrar_sayisi = random_num.count(int(eleman))
        perm += tekrar_sayisi
    return perm

def find_number(random_num, num):
    dot = 0
    random_digit = [int(digit) for digit in str(random_num)]
    num_digit = [int(digit) for digit in str(num)]
    
    for b1, b2 in zip(random_digit, num_digit):
        if b1 == b2:
            dot += 1
    perm = perm_number(random_num, num)
    print(f"Konumu Bulunan: {dot} Karisik:{perm - dot}")
    return dot

random_num = 0
while len(set(str(random_num))) != 4:
    random_num = random.randint(1000, 9999)
while True:
    num = int(input("Sayi tahmininiz:"))
    if 1000 <= num < 10000:
        print("Yanlis bir deger girdin")
    elif find_number(random_num, num) == 4:
        break
print("Sayiyi Buldun")