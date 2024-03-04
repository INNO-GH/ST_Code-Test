import sys
sys.setrecursionlimit(10**6) # python has basic recursion limit 1000 and below change that 
                             # sys.setrecursionlimit(limitnum)
                             

def dfs(now, adj, visit): # Check the visit node from start to end
    if(visit[now] == 1):
        return
    visit[now] = 1
    for neighbor in adj[now]:
        dfs(neighbor, adj, visit)
    return

## 1. Get Input
n, m = map(int, input().split())
adj = []
for i in range(n+1):
    adj.append([])
adjR = []
for i in range(n+1):
    adjR.append([])
for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y) # adj means correct
    adjR[y].append(x) # adjR means reverse
s, t = map(int, input().split())

## 2. Solve by DFS

# 1, 2 find the possible visit node
# 3, 4 judge whether the node is ingoing trap node or not

# 1. S -> T in correct 
fromS = []
for i in range(n+1):
    fromS.append(0)
fromS[t] = 1
dfs(s, adj, fromS)
 
# 2. T -> S in correct
fromT = []
for i in range(n+1):
    fromT.append(0)
fromT[s] = 1
dfs(t, adj, fromT)

# 3. S -> T in reverse
toS = []
for i in range(n+1):
    toS.append(0)
dfs(s, adjR, toS)

# 4. T -> S in reverse
toT = []
for i in range(n+1):
    toT.append(0)
dfs(t, adjR, toT)

## 3. Final Judgement according to above logic
count = 0
for i in range(1, n+1):
    if(fromS[i] and fromT[i] and toS[i] and toT[i]):
        count = count + 1
print(count-2) # Skip home and company
