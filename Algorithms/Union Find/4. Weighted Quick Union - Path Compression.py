class DSU:
    def __init__(self, N):
        self.ids = list(range(N))
        self.szs = [1]*(N)
        self.size = N

    def union(self, p, q):
        pId = self.root(p)
        qId = self.root(q)

        if pId==qId: return
        
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
            self.ids[p] = self.ids[self.ids[p]]
            p = self.ids[p]
        return p

    def rootRecursive(self, p):
        if p==self.ids[p]:
            return p
        self.ids[p] = self.rootRecursive(self.ids[p])
        return self.ids[p]

N = int(input("Please Insert the number of points -> "))
dsu = DSU(N)

while(True):
    method = int(input("1 for union, 2 for find, anything else to close"))
    if method == 1:
        print("Provide two points to union")
        p, q = [int(i) for i in input().split()]

        if not dsu.connected(p, q):
            dsu.union(p, q)
            print(p, " --> ", q)
        else:
            print("Already connected")
    elif method == 2:
        p, q = [int(i) for i in input().split()]
        dsu.connected(p, q)

    else:
        break
print(dsu.ids)