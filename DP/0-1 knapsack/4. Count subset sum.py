# Given an array arr[] of length N and an integer X, the task is to find the number of subsets with a sum equal to X.
# Input: arr[] = {1, 2, 3, 3}, X = 6 
# Output: 3 
# All the possible subsets are {1, 2, 3}, 
# {1, 2, 3} and {3, 3}

# Input: arr[] = {1, 1, 1, 1}, X = 1 
# Output: 4

def recursion(index, total):
    if total==0: return 1
    if index<=0 or total<0: return 0
    
    taken, notTaken = 0,0
    
    if arr[index-1]<=total:
        taken = recursion(index-1, total-arr[index-1])
    notTaken = recursion(index-1, total)
    
    return taken+notTaken
return recursion(n,sum)


memo = [[-1]*(sum+1) for _ in range(n+1)]
def memoization(index, total):
    if index<=0:
        if total==0: return 1
        return 0
    if memo[index][total]!=-1: return memo[index][total]
    
    taken, notTaken = 0,0
    if arr[index-1]<=total:
        taken = memoization(index-1, total-arr[index-1])
    notTaken = memoization(index-1, total)
    
    memo[index][total] = taken + notTaken
    return memo[index][total]
return memoization(n, sum)%(10**9+7)


tab = [[0]*(sum+1) for _ in range(n+1)]
def tabulation(N, SUM):
    for i in range(N+1):
        tab[i][0] = 1
    
    for index in range(1, N+1):
        for total in range(0, SUM+1):
            taken, notTaken = 0,0
            if arr[index-1]<=total:
                taken = tab[index-1][total-arr[index-1]]
            notTaken = tab[index-1][total]
            
            tab[index][total] = taken + notTaken
    return tab[N][SUM]%(10**9+7)
return tabulation(n,sum)

twoRows = [[0]*(sum+1) for _ in range(2)]
def spaceOptimization(N, SUM):
    for i in range(2):
        twoRows[i][0] = 1
    
    toggleIndex = 1
    for index in range(1, N+1):
        for total in range(0, SUM+1):
            taken, notTaken = 0,0
            if arr[index-1]<=total:
                taken = twoRows[toggleIndex^1][total-arr[index-1]]
            notTaken = twoRows[toggleIndex^1][total]
            
            twoRows[toggleIndex][total] = taken + notTaken
        toggleIndex^=1
    return twoRows[toggleIndex^1][SUM]%(10**9+7)
return spaceOptimization(n,sum)

oneRow = [0]*(sum+1)

def superSpaceOptimization(N,SUM):
    oneRow[0] = 1
    for index in range(1, N+1):
        for total in range(SUM,-1,-1):
            taken, notTaken = 0,0
            if arr[index-1]<=total:
                taken = oneRow[total-arr[index-1]]
            notTaken = oneRow[total]
            
            oneRow[total] = taken + notTaken
    return oneRow[SUM]%(10**9+7) 
return superSpaceOptimization(n,sum)