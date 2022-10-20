import sys

n = int(sys.stdin.readline())
t, p = [0 for i in range(n+1)], [0 for i in range(n+1)]
# print(t)

for i in range(n):
    t[i], p[i] = map(int, input().split())

dp = [0 for i in range(n+1)]

print(t)
print(p)
print(dp)

for i in range(n):
    if dp[i] > dp[i+1]:
        dp[i+1] = dp[i]
    if dp[i+t[i]] < dp[i]+p[i]:
        dp[i+t[i]] = dp[i] + p[i]

print(t)
print(p)
print(dp)
print('answer', dp[n])