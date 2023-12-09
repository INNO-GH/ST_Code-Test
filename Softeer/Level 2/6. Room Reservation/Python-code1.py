import sys
## 1. Get N/M
NM = input().split()
N = int(NM[0]);
M = int(NM[1]);

## 2. Get Room's name
room = []
for i in range(N):
    room.append(input())
room.sort() # possible to sort 'char'
for i in range(N): # pre-set the time > and remove them
    room.insert(2*i+1, ['09-10', '10-11', '11-12', '12-13', '13-14', '14-15', '15-16', '16-17', '17-18'])

## 3. Get Reserve Information > Find Room > Remove Reservation available Time
for i in range(M):
    reserve = input().split()
    reserve[1] = int(reserve[1])
    reserve[2] = int(reserve[2])
    for j in range(N):
        if(reserve[0]==room[2*j]):
            for k in range(reserve[2]-reserve[1]):
                if(reserve[1]+k==9): # Be careful that str(9) is not '09'
                    room[2*j+1].remove('09-10')
                else:
                    room[2*j+1].remove(str(reserve[1]+k)+'-'+str(reserve[1]+k+1))  
            break  

## 4. Print Result
flag=0
for i in range(N):
    flag=flag+1 # This is for '-----' 
    print('Room '+room[2*i]+':')
    if(len(room[2*i+1])==0):
        print('Not available')
    else:
        # Time Merge + Print
        timemerge=[]
        j=0
        while(j<len(room[2*i+1])):
            fronttime=room[2*i+1][j][0:2] # [0:2] means 0~1
            lasttime=room[2*i+1][j][3:5]
            j=j+1
            while((j)!=len(room[2*i+1]) and int(lasttime) == int(room[2*i+1][j][0:2])):
                lasttime=room[2*i+1][j][3:5]
                j=j+1
            timemerge.append(fronttime+'-'+lasttime)
        print(str(len(timemerge))+' available:')
        for k in range(len(timemerge)):
            print(timemerge[k])    
    if(flag!=N):
        print('-----')
