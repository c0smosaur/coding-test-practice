import sys

def input():
    return sys.stdin.readline().rstrip()


n = int(input())
origin = n
count = 0

while True:
    temp = 0
    if n < 10:
        n = n*10 + n
    else:
        n = (n % 10) * 10 + (n // 10 + n % 10) % 10
        
    count += 1
    if origin == n:
        break

print(count)