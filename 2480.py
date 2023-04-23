a,b,c = map(int,input().split())
if a == b and b  == c and a == c:
    print(10000+a*1000)
elif a != b and b != c and a != c:
    print(((a if a > b else b) if ((a if a > b else b) > c) else c)*100)
elif a == b and c != b:
    print(1000+a*100)
elif a == c and c != b:
    print(1000+a*100)
elif c == b and a != b:
    print(1000+b*100)