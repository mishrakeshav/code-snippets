class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, index, value):
        index += 1
        while index <= self.size:
            self.tree[index] = (self.tree[index] + value) 
            index += index & -index # gets least significant bit 
    
    def query(self, index):
        result = 0
        while index > 0:
            result = (result + self.tree[index])
            index -= index & -index
        return result
    