class DSU:
    def __init__(self, N):
        self.ids = list(range(N))
        self.size = N

    def union(self, p, q):
        pId = self.ids[p]
        qId = self.ids[q]

        for i in range(N):
            if self.ids[i]==pId:
                self.ids[i]=qId

    def connected(self, p, q):
        return self.ids[p]==self.ids[q]

N = int(input("Please Insert the number of points -> "))
dsu = DSU(N)

while(True):
    p, q = [int(i) for i in input().split()]
    if p==-1 or q==-1:
        break
    if not dsu.connected(p, q):
        dsu.union(p, q)
        print(p, " --> ", q)