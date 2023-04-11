l = []
for i in range(1,29):
    t = int(input())
    t = [t]
    l.extend(t)
lis = []
for j in range(1,31):
    lis.extend([j])
a = [x for x in lis if x not in l]
a.sort()
print(a[0])
print(a[1])
