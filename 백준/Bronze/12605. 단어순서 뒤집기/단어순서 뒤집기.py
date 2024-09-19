import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

for i in range(n):
    case = input().split()
    answer = []
    for j in range(len(case)):
        answer.append(case.pop())
    print(f"Case #{i+1}: "+' '.join(answer))