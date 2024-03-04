import sys
# check i one by one and compare

# 1. Get MNK
MNK=input().split() # list.split() means spliting spring by balnk
M=int(MNK[0])
N=int(MNK[1])
K=int(MNK[2])

# 2. Get Secret Code
secret=input().split()
for i in range(M):
    secret[i]=int(secret[i])

# 3. Get Input Code
Input=input().split()
for i in range(N):
    Input[i]=int(Input[i])

# 4. Check one by one beginning at first
for i in range(N-M+1):
    flag=0
    for j in range(M):
        if(secret[j]==Input[i+j]):
            flag=flag+1
        else:
            break
    if(flag==M):
        print('secret')
        exit() ## finishing
print('normal')
