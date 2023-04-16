a = int(input())
b = int(input())
B = []
sum = 0
for i in range(0,b):
    A = list(map(int,input().split()))
    B.extend(A)
for i in range(0,b):
    C = int(B[2*i])*int(B[2*i+1])
    sum = sum + C
if a == sum :
    print("Yes")
else:
    print("No")