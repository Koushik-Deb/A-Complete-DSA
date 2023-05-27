class DSU:
    def __init__(self, N):
        self.ids = list(range(N))
        self.szs = [1]*(N)
        self.size = N

    def union(self, p, q):
        pId = self.root(p)
        qId = self.root(q)

        if self.szs[pId]>=self.szs[qId]:
            self.ids[qId] = pId
            self.szs[pId] += self.szs[qId]
        else:
            self.ids[pId] = qId
            self.szs[qId] += self.szs[pId]

    def connected(self, p, q):
        return self.root(p)==self.root(q)

    def root(self, p):
        while(p!=self.ids[p]):
            p = self.ids[p]
        return p
        
N = int(input("Please Insert the number of points -> "))
dsu = DSU(N)

while(True):
    p, q = [int(i) for i in input().split()]
    if p==-1 or q==-1:
        break
    if not dsu.connected(p, q):
        dsu.union(p, q)
        print(p, " --> ", q)