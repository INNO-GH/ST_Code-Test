import sys
import copy

# global variable in open space and local variable in user function

# be careful that list1 = list2 means list1 is a refernece of list2
# so when we want to just put value, we should use import copy and copy.deepcopy(list2)

## 2. Linked Block Making Fuction
def LB(data, blocknum, blocklink): # Use DFS
    blocklink.append(blocknum)
    i=int(blocknum/N)+2*N # Remember making i j with N 
    j=blocknum%N
    if(i > 2*N and data[i-1][j]==data[i][j] and blocklink.count(blocknum-N)==0):
        LB(data, blocknum-N, blocklink)
    if(j > 0 and data[i][j-1]==data[i][j] and blocklink.count(blocknum-1)==0):
        LB(data, blocknum-1, blocklink)
    if(i < N-1+2*N  and data[i+1][j]==data[i][j] and blocklink.count(blocknum+N)==0):
        LB(data, blocknum+N, blocklink)
    if(j < N-1 and data[i][j+1]==data[i][j] and blocklink.count(blocknum+1)==0):
        LB(data, blocknum+1, blocklink)  

## 3. Score Fuction
def Score(blocklink): # Calculate width and height without considering shape, and multiply them
    hor=[]
    ver=[]
    for k in blocklink:
        if(hor.count(int(k/N))==0):
            hor.append(int(k/N))
        if(ver.count(k%N)==0):
            ver.append(k%N)
    return len(blocklink)+len(hor)*len(ver)

## 4. Replace Function
def Replace(data, blocklink):
    blocklink.sort() # Move to down in vertical line
    for k in blocklink:
        i=int(k/N)+2*N
        j=k%N
        for l in range(i,0,-1):
            data[l][j]=data[l-1][j]

## 5. Coplete in 1 block
def Simple_Complete(data, blocknum, score, flag, P): # Use DFS
    blocklink=[]
    LB(data, blocknum, blocklink)
    for i in blocklink:
        P.append(i)
    score=score+Score(blocklink) # Save score and export in last step
    if(flag==3): 
        score_set.append(score)
        return
    else:
        Replace(data, blocklink)
        b=[]
        for i in range(N*N):
            if(b.count(i)==0):
                data_copy_2=copy.deepcopy(data)    
                Simple_Complete(data_copy_2, i, score, flag+1, b)

## 1. Get input
N=int(input())
data=[]
score_set=[]
for i in range(3*N):
    data.append(input().split())
    for j in range(N):
        data[i][j]=int(data[i][j])
a=[] # a and b is for avoiding same result case
for i in range(N*N):
    if(a.count(i)==0):
        data_copy_1=copy.deepcopy(data)
        Simple_Complete(data_copy_1,i,0,1,a)
print(max(score_set))

# It is good way to make each fuction respectively and incorporate them with connecting logic
