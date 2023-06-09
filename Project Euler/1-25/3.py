import math

def factorize(n):
    res = []
    while n % 2 == 0:
        res.append(2)
        n //= 2
    limit = math.sqrt(n+1)
    i = 3
    while i <= limit:
        if n % i == 0:
            res.append(i)
            n //= i
            limit = math.sqrt(n+i)
        else:
            i += 2
    if n != 1:
        res.append(n)
    return res

print(max(factorize(600851475143)))
