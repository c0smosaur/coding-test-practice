num = int(input())
lst = sorted(list(map(int, input().split())))
x = int(input())

count = 0
start = 0
end = num-1

while start < end:
    sum_ = lst[start] + lst[end]
    if sum_ == x:
        count += 1
        start += 1
        end -= 1
    elif sum_ < x:
        start += 1
    else:
        end -= 1

print(count)