import sys
def input():
    return sys.stdin.readline().rstrip()

num = int(input())

for _ in range(num):
    test_case = list(input())
    right = list()
    left = list()

    for cmd in test_case:
        if cmd == "<" and left:
            right.append(left.pop())
        elif cmd == ">" and right:
            left.append(right.pop())
        elif cmd == "-" and left:
            left.pop()
        elif cmd != "<" and cmd != ">" and cmd != "-":
            left.append(cmd)
            
    print("".join(left+right[::-1]))