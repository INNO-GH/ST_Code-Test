import sys

def dfs(color, left, right, bottom, top): # dfs is a good solution when we should operate many cases in data
    global minArea
    for point in color_list[color]:
        x, y = point[0], point[1]
        leftN, rightN = min(left, x), max(right, x) # expand the extent to contain test point all
        bottomN, topN = min(bottom, y), max(top, y) # min(a, b) max(a, b) bring us samller and larget data directly
        area = (rightN-leftN)*(topN-bottomN)
        if(minArea > area): # if area is larger than minarea, this case cannot be the minarea
            if(color == K-1):
                minArea = area
            else:
                dfs(color+1, leftN, rightN, bottomN, topN)
    return

# 1. Get Input and Make color_list 
N, K = map(int, sys.stdin.readline().split()) # Use sys.stdin.readline().split() instead of input().split() (Time)
color_list=[]                                 # (sys.stdin.readline() brings \n too, but .split() delete it)
for i in range(K):                            # (and sys.stdin.readline() don't use prompt message)
    color_list.append([])                     # map(int, list) divide list and make each int type
for i in range(N):                            # list(divide) make elements list
    get_input = list(map(int, sys.stdin.readline().split()))
    color_list[get_input[2]-1].append(get_input[:2])
while(color_list.count([])!=0): # This is for none element's color
    color_list.remove([])
K = len(color_list)

# 2. Solve by DFS
minArea = 2000*2000
dfs(0, 1000, -1000, 1000, -1000)
print(minArea)

