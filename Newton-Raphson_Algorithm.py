def newton_raphson(f, f_prime, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        fpx = f_prime(x)
        if fpx == 0:
            break
        x -= fx / fpx
    return x

f = lambda x: x**2 - 2
f_prime = lambda x: 2*x

print(newton_raphson(f, f_prime, 1))
