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


def count_prime_squares_in_range(l, r):
    limit = int(r ** 0.5)
    primes = sieve_of_eratosthenes(limit)
    prime_squares = set([p * p for p in primes])

    count = 0
    for square in prime_squares:
        if l <= square <= r:
            count += 1

    return count


def all_factors(num):
    """
    # Example usage
    num = 36
    print(all_factors(num))  # Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]
    """
    factors = []
    
    # Check for each number from 1 to sqrt(num)
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            factors.append(i)
            if i != num // i:  # Avoid adding the square root twice
                factors.append(num // i)
    
    return sorted(factors)


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
            101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
            211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
            307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
            401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
            503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
            601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
            701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
            809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
            907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]



"""
Bézout's identity—Let a and b be integers with greatest common divisor d. 
Then there exist integers x and y such that ax + by = d. 
Moreover, the integers of the form az + bt are exactly the multiples of d.
"""