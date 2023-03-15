import random

x=100

def is_prime(n, k=50):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

while True:
    num = random.randint(10**x, 10**(x+1)-1)
    if is_prime(num):
        print(num)
        x+=1
