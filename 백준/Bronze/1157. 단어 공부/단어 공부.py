import sys

def input():
    return sys.stdin.readline().rstrip()

word = input().lower()
freq = dict()

for letter in word:
    if letter not in freq:
        freq[letter] = 1
    else:
        freq[letter] += 1

max_freq = max(freq.values())
max_letters = [letter for letter, count in freq.items() if count == max_freq]

if len(max_letters) > 1:
    print("?")
else:
    print(max_letters[0].upper())