import math 
MOD = 10**9 + 7
P = 256
def calculate_hash(word):
    prev = 0
    curr = 0
    for w in word:
        curr = (prev*P + ord(w))%MOD
        prev = curr
    return curr

def calculate_rolling_hash(prev, w):
    return (prev*P + ord(w))%MOD

def calculate_rev_rolling_hash(prev, w,p):
    return (p*ord(w) +  prev)%MOD



def chf(word):
    p = 1
    h = 0 
    for w in word:
        h += p*ord(w) 
        p *= P 
        p %=MOD  
    return h


        



        