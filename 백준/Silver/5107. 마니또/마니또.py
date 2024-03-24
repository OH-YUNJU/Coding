class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True

def count_chains(relationships):
    n = len(relationships)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i+1, n):
            if relationships[i][1] == relationships[j][0] or relationships[j][1] == relationships[i][0]:
                uf.union(i, j)
    
    chains = set()
    for i in range(n):
        chains.add(uf.find(i))
    
    return len(chains)

test_case = 1
while True:
    N = int(input())
    if N == 0:
        break
    
    relationships = [input().split() for _ in range(N)]
    chains = count_chains(relationships)
    print(test_case, chains)
    test_case += 1
