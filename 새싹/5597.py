arr = []
for i in range(1,31):
    arr.append(i)
for _ in range (28):
    n = int(input())
    arr.remove(n)

print(min(arr))
print(max(arr))