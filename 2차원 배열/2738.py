a,b = map(int,input().split())
k = list(map(int,input().split()))
for i in range(a*2-1):
    n = list(map(int,input().split()))
    k.extend(n)
for j in range(0,b):
    print(k[j]+k[a*b+j],end=" ")
print()
for j in range(b,(a-1)*b):
    print(k[j]+k[a*b+j],end=" ")
print()
for j in range((a-1)*b,a*b):
    print(k[j]+k[a*b+j],end=" ")
    