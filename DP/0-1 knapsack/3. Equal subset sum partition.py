# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

arr = nums
total = sum(nums)

if total%2: return False
target = total//2
n = len(nums)

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

return superSpaceOptimization(n, target)