# Given an array of non-negative integers and an integer sum. We have to tell whether there exists any subset in an array whose sum is equal to the given integer sum.

# Examples:

# Input: arr[] = {3, 34, 4, 12, 3, 2}, sum = 7
# Output: True
# Explanation: There is a subset (4, 3) with sum 7.

# Input: arr[] = {2, 2, 2, 3, 2, 2}, sum = 10
# Output: True

arr = [3,34,4,12,3,2]
target = 10
n = len(arr)

def recursion(index, total):
    if total==0: return True
    if index<=0 or total<0: return False

    taken, notTaken = False, False

    if arr[index-1]<=total:
        taken = recursion(index-1, total-arr[index-1])
    notTaken = recursion(index-1, total)

    return taken or notTaken


memo = [[-1]*(target+1) for _ in range(n+1)]
def memoization(index, total):
    if total==0: return True
    if index<=0 or total<0: return False
    if memo[index][total]!=-1: return memo[index][total]

    taken, notTaken = False, False

    if arr[index-1]<=total:
        taken = memoization(index-1, total-arr[index-1])
    notTaken = memoization(index-1, total)

    memo[index][total] = taken or notTaken
    return memo[index][total]

tab = [[False]*(target+1) for _ in range(n+1)]
def tabulation(n, target):
    for i in range(n+1):
        tab[i][0] = True

    for index in range(1, n+1):
        for total in range(1, target+1):
            taken, notTaken = False, False

            if arr[index-1]<=total:
                taken = tab[index-1][total-arr[index-1]]
            notTaken = tab[index-1][total]

            tab[index][total] = taken or notTaken
    return tab[n][target]

twoRows = [[False]*(target+1) for _ in range(2)]
def spaceOptimization(n, target):
    for i in range(2):
        twoRows[i][0] = True
    toggleIndex = 1
    for index in range(1, n+1):
        for total in range(1, target+1):
            taken, notTaken = False, False

            if arr[index-1]<=total:
                taken = twoRows[toggleIndex^1][total-arr[index-1]]
            notTaken = twoRows[toggleIndex^1][total]

            twoRows[toggleIndex][total] = taken or notTaken
        toggleIndex^=1
    return twoRows[toggleIndex^1][target]

oneRow = [False]*(target+1)
oneRow[0] = True
def superSpaceOptimization(n, target):
    for index in range(1, n+1):
        for total in range(target,-1,-1):
            taken, notTaken = False, False

            if arr[index-1]<=total:
                taken = oneRow[total-arr[index-1]]
            notTaken = oneRow[total]
            oneRow[total] = taken or notTaken
    return oneRow[target]




print(recursion(n,target))
print(memoization(n, target))
print(tabulation(n, target))
print(spaceOptimization(n, target))
print(superSpaceOptimization(n, target))