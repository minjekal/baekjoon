a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = list(map(int,input().split()))
e = list(map(int,input().split()))

A = int(a[0])+int(a[1])+int(a[2])+int(a[3])
B = int(b[0])+int(b[1])+int(b[2])+int(b[3])
C = int(c[0])+int(c[1])+int(c[2])+int(c[3])
D = int(d[0])+int(d[1])+int(d[2])+int(d[3])
E = int(e[0])+int(e[1])+int(e[2])+int(e[3])

s = [A,B,C,D,E]
s.sort()
if s[4] == A:
    k = 1
elif s[4] == B:
    k = 2
elif s[4] == C:
    k = 3
elif s[4] == D:
    k = 4
elif s[4] == E:
    k = 5
print(k,s[4],sep=" ")
