import sys
# easy problem -> but consider very large number regarding time or memory overflow

## 1. Get K,P,N
KPN=input().split()
K=int(KPN[0])
P=int(KPN[1])
N=int(KPN[2])

## 2. print result -> We can just use P**N, but it could be VLN -> So multiply P one by one + pre-divide 1000000007 
for i in range(N): 
    K=(K*P)%1000000007
print(K)
