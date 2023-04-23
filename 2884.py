x, y = input().split()
x = int(x)
y = int(y)
if x >= 0 and y >= 45:
        print(x,y-45,sep=" ")
elif x > 0 and y <= 45:
        print(x-1, 60-(45-y),sep=" ") 
elif x == 0 and y < 45:
        print(23,60-(45-y),sep=" ")  