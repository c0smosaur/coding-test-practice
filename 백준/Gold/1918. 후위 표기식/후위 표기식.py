import sys

def input():
    return sys.stdin.readline().rstrip()

infix = input()
answer = []
stack = []
priority = {'+':1, '-':1, '*':2, '/':2}

for s in infix: 
    if s.isalpha(): # operand
        answer.append(s)
    elif s == '(': # left parenthesis
        stack.append(s)
    elif s == ')': # right parenthesis
        while stack and stack[-1] != "(":
            answer.append(stack.pop())
        stack.pop()
        
    else: # operator
        while stack and stack[-1] != "(" and priority[stack[-1]] >= priority[s]:
            answer.append(stack.pop())
        stack.append(s)

while stack:
    answer.append(stack.pop())

print(''.join(answer))