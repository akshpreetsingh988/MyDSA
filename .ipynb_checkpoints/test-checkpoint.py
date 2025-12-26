if __name__ == "__main__":
    n = 100
    primes = [True] * (n + 1)

    primes[0] = False
    primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p] == True:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    print(primes)
    for i in range()