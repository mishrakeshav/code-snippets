import math
import string
from typing import List

class RollingHash:

    def __init__(self, s,p = 256, MOD = 10**9 + 7):
        self.prefix_hashes = None
        self.powers = None
        self.p = p
        self.s = s
        self.MOD = MOD
        self.calc_hash()

    def calc_hash(self):
        n = len(self.s)
        prefix_hashes = [0] * (n + 1)
        powers = [1] * (n + 1)
        p = self.p
        MOD = self.MOD

        for i in range(1, n + 1):
            powers[i] = (powers[i - 1] * p) % MOD

        for i in range(n):
            prefix_hashes[i + 1] = (prefix_hashes[i] + (ord(self.s[i]) - ord('a') + 1) * powers[i]) % MOD

        self.prefix_hashes = prefix_hashes
        self.powers = powers

    def get_substring_hash(self, l, r):
        mod = self.MOD
        hash_value = (self.prefix_hashes[r + 1] - self.prefix_hashes[l] + mod) % mod
        return (hash_value * pow(self.powers[l], mod - 2, mod)) % mod


def calculate_rolling_hash(word):
    MOD = 10 ** 9 + 7
    P = 256
    curr = 0
    for w in word:
        curr = (curr*P + ord(w))%MOD
    return curr

def calculate_reverse_rolling_hash(word):
    MOD = 10 ** 9 + 7
    P = 256
    p = 1
    curr = 0
    for w in word:
        curr = (curr + p*ord(w)) % MOD
        p *= P
    return curr


################## get substring hash ##################

def precompute_hashes(s: str, p: int = 31, mod: int = 10 ** 9 + 7):
    n = len(s)
    prefix_hashes = [0] * (n + 1)
    p_powers = [1] * (n + 1)

    # Precompute powers of p (i.e., p^0, p^1, p^2, ..., p^n) modulo mod
    for i in range(1, n + 1):
        p_powers[i] = (p_powers[i - 1] * p) % mod

    # Precompute prefix hashes
    for i in range(n):
        prefix_hashes[i + 1] = (prefix_hashes[i] + (ord(s[i]) - ord('a') + 1) * p_powers[i]) % mod

    return prefix_hashes, p_powers


def get_substring_hash(l: int, r: int, prefix_hashes, p_powers, mod: int = 10 ** 9 + 7):
    # Hash of substring s[l:r+1] using the prefix hashes
    hash_value = (prefix_hashes[r + 1] - prefix_hashes[l] + mod) % mod
    # Normalize by dividing by p^(l), i.e., multiplying by the modular inverse of p^l
    # pow(p_powers[l], mod - 2, mod) calculated module inverse of p^l
    # Proof :
    # module inverse of (a⋅b) mod m = 1
    # fermat's little theorem : if m is a prime number then a ^ (m - 1) = 1 mod m
    # => a ^ (m - 2) = a^(-1) mod m
    # so by calculating pow(p_powers[l], mod - 2, mod) we get module inverse of (p^l)
    return (hash_value * pow(p_powers[l], mod - 2, mod)) % mod

################## ----------------- ##################




def rabin_karp(pattern: str, text: str) -> List[int]:
    prime_base = 31
    mod = int(1e9 + 9)
    pattern_len, text_len = len(pattern), len(text)

    # Precompute powers of prime_base modulo mod
    prime_powers = [1] * max(pattern_len, text_len)
    for i in range(1, len(prime_powers)):
        prime_powers[i] = (prime_powers[i - 1] * prime_base) % mod

    # Compute prefix hashes for the text
    text_hashes = [0] * (text_len + 1)
    for i in range(text_len):
        text_hashes[i + 1] = (text_hashes[i] + (ord(text[i]) - ord('a') + 1) * prime_powers[i]) % mod

    # Compute the hash for the pattern
    pattern_hash = 0
    for i in range(pattern_len):
        pattern_hash = (pattern_hash + (ord(pattern[i]) - ord('a') + 1) * prime_powers[i]) % mod

    occurrences = []
    for i in range(text_len - pattern_len + 1):
        # Get current substring hash
        current_hash = (text_hashes[i + pattern_len] - text_hashes[i] + mod) % mod
        # Compare it with the pattern hash
        # the current_hash need to be multiplied by module inverse of prime_powers[i] to get the correct hash
        # instead of that we multiply pattern_hash by prime_powers[i] for comparison
        if current_hash == (pattern_hash * prime_powers[i]) % mod:
            occurrences.append(i)

    return occurrences


##### KMP Algorithm #####


def prefix_function(s):
    n = len(s)
    pi = [0 for i in range(n)]

    for i in range(1,n):
        j = pi[i-1]
        while j > 0 and s[i] != s[j]:
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


def kmp_search(text: str, pattern: str) -> list:
    n, m = len(text), len(pattern)
    lps = prefix_function(pattern)
    i = 0  # index for text
    j = 0  # index for pattern
    result = []  # to store the starting indices of matches

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            result.append(i - j)  # found a match, record the starting index
            j = lps[j - 1]  # continue to check for more matches

        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result


### Z Function

def z_function(s):
    n = len(s)
    z = [0] * n  # Initialize the Z-array with zeros
    l, r = 0, 0  # Initialize the window [l, r]

    for i in range(1, n):
        if i <= r:
            # Reuse previous computations to avoid recalculating
            z[i] = min(r - i + 1, z[i - l])

        # Try to extend the Z[i] value by comparing characters
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        # Update the window if the new Z-box extends beyond r
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1

    return z


def check_lexicographically_largest(s1, s2):
    """
    checks if s1 is lexicographically larger than s2
    :param s1:
    :param s2:
    :return:
    """
    for idx in range(min(len(s1), len(s2))):
        if s1[idx] > s2[idx]:
            return True
        elif s1[idx] < s2[idx]:
            return False
    return len(s1) > len(s2)