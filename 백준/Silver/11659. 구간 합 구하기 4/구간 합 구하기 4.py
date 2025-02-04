import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
num = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[0] = num[0]

for i in range(1, n + 1):
    dp[i] = num[i - 1] + dp[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    answer = dp[j] - dp[i - 1]

    print(answer)    