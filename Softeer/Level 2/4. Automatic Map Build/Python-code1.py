import sys
## Just mathmatical calculation
## 0. 2*2 / 1. 3*3 / 2. 5*5  / 3. 9*9 5. -> answer = [(pre)+(pre-1)]^2 # Implement this by using recursive(Stack)!
## We should think data structure!

## Global vs Local in python = threshhold is 'User Function' (C is 'Function'. It is difference)

def recur(num):
    global i # Special Case => Make 'i=' not Local-Declare&Puttung but just Putting
    i=i+1
    num=num+(num-1)
    if(i==N):
        return num*num
    else:
        return recur(num)

N=int(input()) # don't foget that we get value by char! int(input())
i=0
print(recur(2))
