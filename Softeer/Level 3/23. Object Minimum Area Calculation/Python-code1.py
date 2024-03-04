import sys

def max_value(XorY): # Function that extract max and min value from data
    maxx = -1000
    for i in range(K):
        if(maxx < color_list[i][2*counter[i]+XorY]):
            maxx = color_list[i][2*counter[i]+XorY]
    return maxx

def min_value(XorY):
    minn = 1000
    for i in range(K):
        if(minn > color_list[i][2*counter[i]+XorY]):
            minn = color_list[i][2*counter[i]+XorY]
    return minn

# 1. Get Input and Make color_list
N, K = map(int, sys.stdin.readline().split())
color_list=[]
for i in range(K):
    color_list.append([])
for i in range(N):
    get_input = list(map(int, sys.stdin.readline().split()))
    color_list[get_input[2]-1].append(get_input[0])
    color_list[get_input[2]-1].append(get_input[1])
while(color_list.count([])!=0):
    color_list.remove([])
K = len(color_list)

# 2. Make Possible Answer List
possible_answer = 4000000

# 3. Just Pick random K point
# And Pick horizontal max and min
# Check if vertical is also max and min
counter = [] # Use counter and loop for operating many cases in data
for i in range(K):
    counter.append(0)
multiply_total = 1
for i in range(K):
    multiply_total = multiply_total * int(len(color_list[i])/2) 
for multiply in range(multiply_total):
    if(possible_answer == 0):
        break
    for i in range(K):
        counter[i] = multiply%int(len(color_list[i])/2) # Mathmatical Calculation about each color's index
        multiply = int(multiply/(int(len(color_list[i])/2)))
    answer = (max_value(0)-min_value(0))*(max_value(1)-min_value(1))
    if(possible_answer > answer):
        possible_answer = answer
print(possible_answer)


