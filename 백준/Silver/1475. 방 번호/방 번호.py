import sys
import math

room_num = sys.stdin.readline().rstrip()
dic = {str(i):0 for i in range(10)}

for num in room_num:
    dic[num] += 1

six_nine_count = dic['6'] + dic['9']
dic['6'] = math.ceil(six_nine_count/2)

del dic['9']

print(max(dic.values()))