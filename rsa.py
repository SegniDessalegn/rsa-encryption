import math
import random


def is_prime(num):
    if num % 2 == 0:
        return False
    n = 3
    while n < math.ceil(math.sqrt(num)):
        if num % n == 0:
            return False
        n += 2
    return True


def large_prime_generator():
    pass




def isPrime(n, k):
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range(k):
            a = random.randint(2, n - 2)
            if pow(a, n - 1, n) != 1:
                return False
    return True


def generate():
    while True:
        num = random.randint(2 ** 10, 2 ** 11)
        if isPrime(num, 3):
            return num


def gcd(x, y):
    while (y):
        x, y = y, x % y
    return x


def mod(a, b):
    if b > a:
        return b % a
    return a % b




print("generating prime numbers...")
p = generate()
q = generate()

print("p", p)
print("q", q)

N = p * q
phi = (p - 1) * (q - 1)
print("phi", phi)
print("generating public key...")
while True:
    i = random.randint(2, phi)
    if phi % i == 0 or phi % N == 0:
        continue
    if gcd(i, phi) == 1 and gcd(i, N) == 1:
        e = i
        break

# for i in range( 2,phi):
#     if gcd(i, phi) == 1:# and gcd(i, N) == 1
#         e = i
#         break

print("public key")
print(e, "=============", N)
print("generating private key...")
d = 2
while True:
    # d=random.randint(2,phi)
    if mod(e * d, phi) == 1 and d>phi//e:
        break
    d += 1

def find_d(e,phi):
    global i,d
    start_position=(phi//e)
    gap=start_position%phi
    while True:
        current_value=(start_position)+(gap*i)+e
        if mod(current_value, phi) == 1:
            return current_value//e
        i+=1
# d=find_d(e,phi)

print("private key")
print(d, "===================", N)

alphabet="abcdefghijklmnopqrstuvwxyz "
message=input("enter the message you want to encrypt")
print("messege:", message)
encrypted=[]
cipher_text=""
for i in range(len(message)):
    for j in range(len(alphabet)):
        if message[i]==alphabet[j]:
            letter=j
            encrypted_shift=pow(letter, e, N)
            encrypted.append(encrypted_shift)
print("encryption:", encrypted)

for i in range(len(encrypted)):
    cipher_text+=alphabet[encrypted[i] % 27]
decrypted=[]
plain_text=""
for i in range(len(encrypted)):
    decrypted_shift=pow(encrypted[i], d, N)
    decrypted.append(decrypted_shift)
print("decryption:", decrypted)
for i in range(len(decrypted)):
    plain_text+=alphabet[decrypted[i] % 27]

print("the cipher text is:", cipher_text)
print("the plain text is:", plain_text)
