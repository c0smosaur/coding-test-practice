num = int(input())
lst = list(map(int, input().split()))
v = int(input())

count = 0

for n in lst:
    if n == v:
        count += 1
        
print(count)