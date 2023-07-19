from collections import defaultdict;

def findResult(n, arr):
    dt = defaultdict(int)

    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            dt[arr[i]+arr[j]] += 1
    
    result = None
    for key, val in dt.items():
        if result==None:
            result = key
        if val>dt[result]:
            result = key

    arr.sort()
    first, last = 0,n-1
    count = 0
    while(first<last):
        val = arr[first]+arr[last]
        if val == result:
            count+=1
            first+=1
            last-=1
        elif val>result:
            last-=1
        else:
            first+=1

    print("result" ,count)

T = int(input())
for _ in range(T):
    length = int(input())
    arr = [int(i) for i in input().split()]

    findResult(length,arr)