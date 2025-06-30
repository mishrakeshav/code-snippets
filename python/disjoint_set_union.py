class UnionFind:
    def __init__(self, size):
        # Initialize parent and rank arrays
        self.parent = [i for i in range(size)]  # Each node is initially its own parent
        self.rank = [0] * size  # Rank is used to keep track of tree depth
    
    def find(self, x):
        # Path compression optimization
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Recursively find the root and compress the path
        return self.parent[x]
    
    def union(self, x, y):
        # Find roots of the elements
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            # Union by rank optimization
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
