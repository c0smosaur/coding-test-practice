import sys

def input():
    return sys.stdin.readline().rstrip()

n, p = map(int, input().split())
strings = [[] for _ in range(6)]
moves = 0

for _ in range(n):
    note, fret = map(int, input().split())
    string = strings[note-1]
    
    while string and string[-1] > fret:
        string.pop()
        moves += 1
        
    if not string or string[-1] < fret:
        string.append(fret)
        moves += 1
                
print(moves)
