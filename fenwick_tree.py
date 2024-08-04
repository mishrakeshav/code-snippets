class FenwickTree:

    def __init__(self, arr):
        """
        :param arr: arr should be 1 index based
        """
        self.tree = [i for i in arr]
        i = 1
        while i < len(self.tree):
            j = i + self.lsb(i)
            if j < len(self.tree):
                self.tree[j] += self.tree[i]
            i += 1

    @staticmethod
    def lsb(num):
        return num & -num

    def prefix_sum(self, idx):

        i = idx
        res = 0
        while i != 0:
            res += self.tree[i]
            i &= ~self.lsb(i)  # Equivalently, i = i - self.lsb(i)
        return res

    def range_sum(self, i, j):
        return self.prefix_sum(j) - self.prefix_sum(i - 1)

    def add(self, i, v):
        while i < len(self.tree):
            self.tree[i] += v
            i = i + self.lsb(i)

    def set(self, i, v):
        self.add(i, v - self.range_sum(i, i))
