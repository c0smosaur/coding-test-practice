import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

if n == 1:
    print(1)
    exit(0)

dp = [0] * (n + 1)
dp[1] = 1

if n > 1:
    dp[2] = 3

for i in range(3, n + 1):
    dp[i] = (2 * dp[i - 2] + dp[i - 1]) % 10007

print(dp[n])