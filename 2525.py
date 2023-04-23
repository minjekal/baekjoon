x, y = input().split()
x = int(x)
y = int(y)
z = int(input())
k = z//60 
if z + y < 60:
    print(x,z+y,sep=" ")
elif z + y == 60:
    if x+k == 23:
        print(0,0,sep=" ")
    else:
        print(x+1,0,sep=" ")    
elif z + y > 60 and x+k < 23:
    if z-60*k+y == 60:
        print(x+k+1,0,sep=" ")
    if z-60*k+y < 60:
        print(x+k,z-60*k+y,sep=" ")
    if z-60*k+y > 60:
        print(x+k+1,z-60*(k+1)+y,sep=" ")
elif z + y > 60 and x+k == 23:
    if z-60*k+y == 60:
        print(0,0,sep=" ")
    if z-60*k+y < 60:
        print(x+k,z-60*k+y,sep=" ")
    if z-60*k+y > 60:
        print(0,z-60*(k+1)+y,sep=" ")
elif z + y > 60 and  x+k > 23 :
    if z-60*k+y == 60:
        print(x+k-23,0,sep=" ")
    if z-60*k+y < 60:
        print(x+k-24,z-60*k+y,sep=" ")
    if z-60*k+y > 60:
        print(x+k-23,z-60*(k+1)+y,sep=" ")