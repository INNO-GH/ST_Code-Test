import sys
import copy

# It is good to reduce O-Notation

# 1. Get Input
N = int(input())
result = []
for i in range(3):
    result.append(list(map(int, sys.stdin.readline().split())))
result.append([]) # adding sum result
for i in range(N):
    add = 0
    for j in range(3):
        add = add + result[j][i]
    result[3].append(add)

## 2. Give their Rank - Utilize Counting Sort (score range is much smaller)
for k in range(4):
    counter = []  # making counter                
    for i in range(3001):
        counter.append(0)
    for i in range(N):  # we can access to score index directly  
        counter[result[k][i]] = counter[result[k][i]] + 1
    rank = []
    index = 1
    for i in range(3000, -1, -1): # extract ranking information  
        if(counter[i]!=0):
            rank.append([i, index])
            index = index + counter[i]
    for i in range(N): # N data finding their own score and rank  
        for point in rank:
            if(point[0] == result[k][i]):
                print(point[1], end=' ')
                break
    print()

