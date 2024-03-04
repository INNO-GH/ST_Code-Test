import sys
## 1. just represent number in digital form (0,1) >> 2. Compare 2 different digit
## I will use 1,2,3,4,5,6,7,8 from left to right, and from top to bottom

## make_digit + digit_one => chage number to digital sign

def make_digit(number_total): # Collect the digit number one by one and Return them
    digit=[]
    for i in range(len(number_total)):
        digit.append(digit_one(number_total[i]))
    return digit

def digit_one(number): # Make one digit number 
    if(number=='0'):
        onedigit=['1','1','1','0','1','1','1']
    if(number=='1'):
        onedigit=['0','0','0','0','0','1','1']
    if(number=='2'):
        onedigit=['0','1','1','1','1','1','0']
    if(number=='3'):
        onedigit=['0','0','1','1','1','1','1']
    if(number=='4'):
        onedigit=['1','0','0','1','0','1','1']
    if(number=='5'):
        onedigit=['1','0','1','1','1','0','1']
    if(number=='6'):
        onedigit=['1','1','1','1','1','0','1']
    if(number=='7'):
        onedigit=['1','0','1','0','0','1','1']
    if(number=='8'):
        onedigit=['1','1','1','1','1','1','1']
    if(number=='9'):
        onedigit=['1','0','1','1','1','1','1']
    return onedigit

## 1. Get the number of case and make two_digit list
## 2. and then compare two digital number

T=int(input())
for i in range(T):
    two_number=input().split()
    two_digit=[]
    two_digit.append(make_digit(two_number[0]))
    two_digit.append(make_digit(two_number[1]))
    if(len(two_digit[0]) < len(two_digit[1])): # Condiser the case when the numbers have different length
        for j in range(len(two_digit[1])-len(two_digit[0])):
            two_digit[0].insert(0,['0','0','0','0','0','0','0']) # index -> element
    elif(len(two_digit[1]) < len(two_digit[0])):
        for j in range(len(two_digit[0])-len(two_digit[1])):
            two_digit[1].insert(0,['0','0','0','0','0','0','0'])
    sum=0
    for j in range(len(two_digit[0])): # Compare
        for k in range(7):
            if(two_digit[0][j][k]!=two_digit[1][j][k]):
                sum=sum+1
    print(sum)
