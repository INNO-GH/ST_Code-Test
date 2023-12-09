import sys

## 1. Get NM
NM=input().split()
N=int(NM[0])
M=int(NM[1])

## 2. Make Standard
standard=[]
for i in range(N):
    meter_velo=input().split()
    meter_velo[0]=int(meter_velo[0])
    meter_velo[1]=int(meter_velo[1])
    standard.append(meter_velo)

## 3. Make Test
test=[]
for i in range(M):
    meter_velo=input().split()
    meter_velo[0]=int(meter_velo[0])
    meter_velo[1]=int(meter_velo[1])
    test.append(meter_velo)

## 4. Compare them
maxerror=[]
i=0
j=0
while(i<N and j<M): # We should consider gradual increasement elevation (imagine cut block at bottom)
    if(standard[i][0] <= test[j][0]):
        test[j][0]=test[j][0]-standard[i][0] # - subtract height
        standard[i][0]=0 
        maxerror.append(test[j][1]-standard[i][1])
        i=i+1 # - go to next velocity if elevation==0
        if(test[j][0]==0):
            j=j+1
    else:
        standard[i][0]=standard[i][0]-test[j][0]
        test[j][0]=0
        maxerror.append(test[j][1]-standard[i][1])
        j=j+1
        if(standard[i][0]==0):
            i=i+1

if(max(maxerror)>0): # Exception: Don't exceed any velocity
    print(max(maxerror))
else:
    print(0)
