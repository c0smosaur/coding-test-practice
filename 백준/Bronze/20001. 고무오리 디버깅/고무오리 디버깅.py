import sys

def input():
    return sys.stdin.readline().rstrip()

start = False
prob = 0

if input() == "고무오리 디버깅 시작":
    start = True

while start:
    cmd = input()
    if cmd == "고무오리":
        if prob:
            prob -= 1
        else:
            prob += 2
    elif cmd == "문제":
        prob += 1
    
    elif cmd == "고무오리 디버깅 끝":
        start = False
        if prob != 0:
            print("힝구")
        else:
            print("고무오리야 사랑해")