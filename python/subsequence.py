import bisect


def length_of_lis(nums):
    sub = []
    for num in nums:
        # Find the index to replace or extend
        pos = bisect.bisect_left(sub, num)

        # If num extends the sequence
        if pos == len(sub):
            sub.append(num)
        else:
            sub[pos] = num  # Replace to maintain the smallest element
    return len(sub)


def lis_with_elements(nums):
    n = len(nums)
    parent = [-1] * n  # To track the predecessor of each element in the LIS path
    sub = []  # Stores the indices of the smallest possible end elements

    for i, num in enumerate(nums):
        pos = bisect.bisect_left(sub, num, key=lambda x: nums[x])

        if pos == len(sub):
            sub.append(i)  # Extend the LIS
        else:
            sub[pos] = i  # Replace to maintain smallest ending element

        # Track the parent if it's not the first element in the sequence
        if pos > 0:
            parent[i] = sub[pos - 1]

    # Reconstruct the LIS by backtracking using the parent array
    lis = []
    k = sub[-1]  # Start with the last element in the LIS
    while k != -1:
        lis.append(nums[k])
        k = parent[k]

    lis.reverse()  # Reverse to get the correct order
    return lis