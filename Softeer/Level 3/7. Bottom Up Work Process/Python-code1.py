import sys

# 1. Get Input + Make CBT
H, K, R = map(int, sys.stdin.readline().split())
CBT = []
for i in range(2**(H+1)-1):
    CBT.append([[],[]]) # [0] means the task which came from left / # [1] means the task which came from right 
for i in range(2**(H)-1, 2**(H+1)-1, 1):
    CBT[i] = list(map(int, sys.stdin.readline().split()))

# 2. Work
worksum = 0
for k in range(1, R+1):
    if(k%2==1): # Even Day
        for i in range(H+1): # In i depth, determine how node gives the work to upper
            if(i==0 and len(CBT[2**(i)-1][0])!=0): # - In first depth
                worksum = worksum + CBT[2**(i)-1][0][0]
                del CBT[2**(i)-1][0][0]
            elif(i==H and len(CBT[2**(i)-1])!=0): # - In last depth
                for j in range(2**(i)-1, 2**(i+1)-1, 1):
                    CBT[int((j+1)*0.5)-1][(j+1)%2].append(CBT[j][0]) # remember the index relation between parent and children
                    del CBT[j][0]
            elif(i!=H and len(CBT[2**(i)-1][0])!=0): # In middle depth
                for j in range(2**(i)-1, 2**(i+1)-1, 1):
                    CBT[int((j+1)*0.5)-1][(j+1)%2].append(CBT[j][0][0])
                    del CBT[j][0][0]
    elif(k%2==0): # Odd Day
        for i in range(H+1):
            if(i==0 and len(CBT[2**(i)-1][1])!=0): # if-elif-else just do one execution and go out (elif doesn't filter previous condition)
                worksum = worksum + CBT[2**(i)-1][1][0]
                del CBT[2**(i)-1][1][0]
            elif(i==H and len(CBT[2**(i)-1])!=0):
                for j in range(2**(i)-1, 2**(i+1)-1, 1):
                    CBT[int((j+1)*0.5)-1][(j+1)%2].append(CBT[j][0])
                    del CBT[j][0]
            elif(i!=H and len(CBT[2**(i)-1][1])!=0):
                for j in range(2**(i)-1, 2**(i+1)-1, 1):
                    CBT[int((j+1)*0.5)-1][(j+1)%2].append(CBT[j][1][0])
                    del CBT[j][1][0]
print(worksum)
