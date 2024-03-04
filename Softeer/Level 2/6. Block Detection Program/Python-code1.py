import sys

# Use disjoint set

def findset(index):  
    if(Set[index]<0): ## Case of root of disjoint set
        return index ## Don't forget that I should return index of root
    else:
        return findset(Set[index]) 

def joinset(index1,index2):
        if(findset(index1)!=findset(index2)): ## Just in case when they are not the same set
            Set[findset(index1)]=findset(index2) 

# First, make matrix
N=int(input())
mat=[]
for i in range(N):
    mat.append(input())
# Second, make Set
Set=[]
for i in range(N*N):
    if(mat[int(i/N)][i%N]=='0'):
        Set.append('X')
    else:
        Set.append(-1)
# if data=1 + have around 1 = join set
for i in range(N):
     for j in range(N):
        if(mat[i][j]=='1'): ## Don't forget that we receive data by string type
            if(i!=0 and mat[i-1][j]=='1'):
                joinset(N*(i)+(j),N*(i-1)+(j)) ## index by calulation => N*i+j
            if(j!=0 and mat[i][j-1]=='1'):     ## We should consider the side data
                joinset(N*(i)+(j),N*(i)+(j-1))
            if(i!=N-1 and mat[i+1][j]=='1'):
                joinset(N*(i)+(j),N*(i+1)+(j))
            if(j!=N-1 and mat[i][j+1]=='1'):
                joinset(N*(i)+(j),N*(i)+(j+1))
# print the number of block and the number of inside Set
blocknum=[]
for i in range(N*N):
    if(Set[i]!='X' and Set[i]<0): ## It's good to filter redundant data ('X') clearly
        blocknum.append(1)
        for j in range(N*N):
            if(Set[j]!='X' and Set[j]>=0 and i==findset(j)):
                blocknum[len(blocknum)-1]=blocknum[len(blocknum)-1]+1
blocknum.sort()
print(len(blocknum))
for i in range(len(blocknum)): ## Not len[] but len() OK?
    print(blocknum[i])
    


