import sys

dict = {}
alphabets = "abcdefghijklmnopqrstuvwxyz"

for alphabet in alphabets:
    dict[alphabet] = 0
    
word = list(str(sys.stdin.readline()).rstrip())
for letter in word:
    dict[letter] += 1
    
print(*dict.values())