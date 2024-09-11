# 입력
w1 = input().strip()
w2 = input().strip()

# 답
count = 0

w1count = {}
w2count = {}

# 빈도수 dictionary 생성
for letter in w1:
    if letter in w1count:
        w1count[letter] += 1
    else:
        w1count[letter] = 1

for letter in w2:
    if letter in w2count:
        w2count[letter] += 1
    else:
        w2count[letter] = 1

# 빈도수 차이 구하기
letterset = set(w1count.keys()).union(set(w2count.keys()))

for letter in letterset:
    count1 = w1count.get(letter, 0)
    count2 = w2count.get(letter, 0)
    count += abs(count1 - count2)

print(count)