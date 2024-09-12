import sys
def input():
    return sys.stdin.readline().rstrip()

left = list(input())
right = []

for i in range(int(input())):
    cmd = input()
    if cmd[0] == "L" and left: # 빈 리스트면 False
        right.append(left.pop())
    elif cmd[0] == "D" and right:
        left.append(right.pop())
    elif cmd[0] == "B" and left:
        left.pop()
    elif cmd[0] == "P":
        left.append(cmd[-1])

print(''.join(left+right[::-1]))
        