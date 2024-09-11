import sys

nums = [int(sys.stdin.readline()) for i in range(3)]
num = nums[0]*nums[1]*nums[2]

dict = {str(i):0 for i in range(10)}

for i in str(num):
    dict[i] += 1
    
for v in dict.values():
    print(v)