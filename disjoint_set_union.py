import collections


class UnionFind:
    def __init__(self):
        self.parent = collections.defaultdict(lambda: None)
        self.depth = collections.defaultdict(lambda: 1)

    def find_set(self, v):
        if self.parent[v] == None:
            self.parent[v] = v
        if self.parent[v] == v:
            return v
        self.parent[v] = self.find_set(self.parent[v])
        return self.parent[v]

    def union_sets(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a == b:
            return False
        if self.depth[a] > self.depth[b]:
            a, b = b, a
        self.parent[a] = b
        self.depth[b] += self.depth[a]
        return True
