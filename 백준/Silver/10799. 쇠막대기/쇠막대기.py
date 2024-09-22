import sys

def input():
    return sys.stdin.readline().rstrip()

prob = input()
stack = []
rods = 0

for i in range(len(prob)):
    if prob[i] == '(':
        stack.append(prob[i])
    else: # prob[i] == ')'
        stack.pop()
        if prob[i - 1] == '(':
            rods += len(stack)
        elif prob[i - 1] == ')':
            rods += 1

print(rods)