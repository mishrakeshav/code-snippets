import math 
# Primes 

def primes_up_to(n):
    primes = set(range(2, n + 1))
    for i in range(2, n):
        if i in primes:
            it = i * 2
            while it <= n:
                if it in primes:
                    primes.remove(it)
                it += i

    return primes



def get_prime_factors(n, primes):
    ret = {}
    sq = int(math.sqrt(n))

    for p in primes:
        if n in primes:
            ret[n] = 1
            break

        while n % p == 0:
            ret[p] = ret.get(p, 0) + 1
            n //= p

        if n <= 1:
            break

    return ret


def get_cnt_of_divisors(num):

    cnt = 1
    for val in range(2,int(num**0.5) + 1):
        if num%val == 0:
            cnt += 1
    return cnt


def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if (is_prime[p] == True):
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, limit + 1) if is_prime[p]]
    return primes