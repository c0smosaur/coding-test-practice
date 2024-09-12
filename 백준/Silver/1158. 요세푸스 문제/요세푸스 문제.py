n, k = map(int, input().split())

circle = [i for i in range(1,n+1)]
answer = []

next_index = 0

while n > 0:
    next_index += k
    
    while next_index > n:
        next_index -= n

    next_index = abs(next_index - 1)
        
    element = circle.pop(next_index)
    answer.append(element)
    n -= 1
    
ans = ", ".join(map(str,answer))
print(f"<{ans}>")