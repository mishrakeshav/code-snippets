import math
import string

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






        



        