class SegmentTree:

    def __init__(self, n, data):
        self.n = n
        self.tree = [0 for i in range(2 * n)]
        self.build(data)

    def build(self, data):

        for i in range(self.n):
            self.tree[self.n + i] = data[i]

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        # Update the value at the specified index
        pos = index + self.n
        self.tree[pos] = value

        # Update the segment tree
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[pos * 2] + self.tree[pos * 2 + 1]

    def query(self, left, right):
        # Range sum query from left to right
        # here right is excluded from query so actually query is from left to right - 1 
        left += self.n
        right += self.n
        result = 0

        if left == right:
            return self.tree[left]

        while left < right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2

        return result
