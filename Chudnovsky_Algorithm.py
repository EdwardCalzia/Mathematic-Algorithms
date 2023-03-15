import decimal

def calculate_pi(precision):
    decimal.getcontext().prec = precision
    pi = decimal.Decimal(0)
    k = 0
    while k < precision:
        pi += (decimal.Decimal(-1)**k) * (decimal.Decimal(factorial(6*k))/((factorial(k)**3)*(factorial(3*k)))*(13591409+545140134*k)/(640320**(3*k)))
        k += 1
    pi = pi * decimal.Decimal(10005).sqrt()/4270934400
    pi = pi**(-1)
    return pi

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(calculate_pi(100))
