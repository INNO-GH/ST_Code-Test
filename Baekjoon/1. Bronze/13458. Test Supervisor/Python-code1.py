import sys
import math

## input ##
RoomNum = int(input())
RoomPeople = list(map(int, sys.stdin.readline().split()))
FirstSV, SubSV = map(int, input().split())
Answer = 0

## Calculation ##
for RP in RoomPeople:
    if((RP-FirstSV) < 0):
        Answer = Answer + 1
    else:
        Answer = Answer + 1 + math.ceil((RP - FirstSV)/SubSV)

## Result ##
print(Answer)
