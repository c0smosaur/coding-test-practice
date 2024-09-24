import sys

def input():
    return sys.stdin.readline().rstrip()

line = input()
stack = []

for l in line:
    if l == "(" or l == "[":
        stack.append(l)
    elif l == ")":
        score = 0
        while stack:
            top = stack.pop() 
            if top == "(": # 괄호가 완성된 경우
                stack.append(2 if score == 0 else score * 2) # 괄호 값 계산하여 stack에 추가
                break # 다음 괄호로 넘어감
            elif isinstance(top, int): # top이 숫자일 경우
                score += top # 값을 score에 추가, 새로 top 확인하러 돌아감
            else:
                print(0) # 괄호 완성 x, 숫자도 아닐 경우 올바르지 못한 괄호열
                exit()
        else: # 스택이 비었는데 괄호가 닫힘
            print(0) 
            exit()

    elif l == "]":
        score = 0
        while stack:
            top = stack.pop()
            if top == "[":
                stack.append(3 if score == 0 else score * 3)
                break
            elif isinstance(top, int):
                score += top
            else:
                print(0)
                exit()
        else:
            print(0)
            exit()

answer = 0
for i in stack:
    if isinstance(i, int):
        answer += i
    else:
        print(0)
        exit()

print(answer)