import sys
import copy

def dfs(one, index):
    if(index == M): # combination is created
        superDNA.append(one)
        return
    for i in possible[index]:
        one_copy = copy.deepcopy(one)
        one_copy.append(i)
        dfs(one_copy, index+1)
    return

def pick(count, totalnum, avail): # Judge in totalnum
    for dna in superDNA:
        avail_copy = copy.deepcopy(avail)
        avail_copy.append(dna)
        if(count != totalnum):
            pick(count+1, totalnum, avail_copy)
        elif(count == totalnum):
            judge = []
            for dna in avail_copy:
                for compare in DNA:
                    if(compare in judge):
                        continue
                    flag = 0
                    for i in range(M):
                        if(compare[i] != '.' and dna[i] != compare[i]):
                            flag = 1
                            break
                    if(flag == 0):
                        judge.append(compare)
            if(len(judge) == N): # If clear, print it and exit
                print(totalnum)
                exit()

# 1. Get Input
N, M = map(int, sys.stdin.readline().split())
DNA = []
for i in range(N):
    DNA.append(input())

# 2. Make possible list (one by one digit)
possible = []
for i in range(M):          
    temp = []          # We can detemine whether element is in list or not by using, element in list
    for j in range(N): 
        if(DNA[j][i] not in temp and DNA[j][i] != '.'):
            temp.append(DNA[j][i])
    if(temp == []):
        possible.append(['a']) # Case that all '.' in digit
    else:
        possible.append(temp)

# 3. Make SuperDNA by Possible List - Create all combination
superDNA = []
dfs([], 0)

# 4. from 1 to N, check whether the number of superDNA can cover all DNA, and print answer if right
answer = N
for totalnum in range(1, N):
    pick(1, totalnum, [])
print(answer)
