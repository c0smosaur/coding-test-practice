import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
cards = [str(i) for i in range(1, n+1)]
throwaway = []
cont = len(cards)

if n == 1:
    print(cards[0])
else:
    while cont != 1:
        throwaway.append(cards.pop(0))
        cards.append(cards.pop(0))
        cont -= 1
    
    print(f"{' '.join(throwaway)} {cards[0]}")