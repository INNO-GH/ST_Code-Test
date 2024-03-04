import sys
import heapq ## We can handle list by heapq
             ## heapq.heappush(list, ~) means insertsort
             ## heapq.heappop(list) means deletemin

        ## list.sort() can also sort lists like dictionary 

N = int(input())
TimeList = []
for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    heapq.heappush(TimeList, (end, start)) ## List[~] Application - Tuple(~) can't change but fast

ans = 0
nowend = 0

## Sort list based on end (not start), and judge time from first to last
## - because we can gurantee that the front part of end has no problem
## - because there's no advantage to add next overlap data instead of nowdata     

for i in range(N):
    end, start = map(int, heapq.heappop(TimeList))
    if start >= nowend: 
        nowend = end 
        ans = ans + 1

print(ans)
