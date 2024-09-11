import math

f_dic = {i:0 for i in range(1,7)}
m_dic = {i:0 for i in range(1,7)}

answer = 0

n, k = map(int, input().split())

for i in range(n):
    s_temp, y_temp = map(int, input().split())
    if s_temp == 0:
        f_dic[y_temp] += 1
    else:
        m_dic[y_temp] += 1

for f_v in f_dic.values():
    answer += math.ceil(f_v / k)

for m_v in m_dic.values():
    answer += math.ceil(m_v / k)

print(answer)