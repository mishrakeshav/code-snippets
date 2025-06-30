
def printing_binary_rep(n):
    for k in range(63,-1,-1):
        print((n >> k) & 1,end="")
    print()

# check if it bit is set or not 
num = 20
i = 2
num & (1 << i)


# counting the number of set bits 
count = 0 
num = 15 
for i in range(31,-1,-1):
    if num & (1 << i):
        count += 1

# How to check if a given number is a power of 2 ?
# Properties for numbers which are powers of 2, is that they have one and only 
# one bit set in their binary representation. 
# If the number is neither zero nor a power of two, it will have 1 in more than 
# one place. So if x is a power of 2 then x & (x-1) will be 0.
# eg.-> 16-> 10000 and 15 -> 1111 
# 16&15==0

def is_power_of_two(n):
    return n & (n-1) == 0

#Although the arithmetic operations are fast ,but by bits manipulation 
#we can make them  more faster.
n=5;
n=n>>1;
#divide by two
n=n<<1;


# twos complement 
# https://stackoverflow.com/questions/1049722/what-is-twos-complement