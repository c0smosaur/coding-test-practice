def solution(s):
    stack = []
    answer = True
    
    for par in s:
        if par == "(":
            stack.append(par)
        elif stack:
            stack.pop()
        else:
            return False

    return False if stack else True