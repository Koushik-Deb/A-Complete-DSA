def trickySum(n):
    totalSum = (n*(n+1)//2)
    toMinus = 2*((1<<len(bin(n)[2:]))-1)
    return totalSum - toMinus
    
T = int(input())
while(T):
    n = int(input())
    T-=1
    print(trickySum(n))