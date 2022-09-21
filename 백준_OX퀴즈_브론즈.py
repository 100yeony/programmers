# N = int(input())
#
# answer = 0
# for i in range(0, N):
#     test = input().split('X')
#     print(test)
#     for i in test:
#
#         if i == 'O':
#             answer += 1


import sys

answer = 0
n = int(input())
# case = input()
# score = [case for x in range(n)]
# print(score)

# score = ''
# for i in range(n):
#     case = str(sys.stdin.readline())
#     score += case

# score = [input() for x in range(n)]
# print(score)

for i in range(n):
    score = input()
    cnt, answer = 0, 0
    for j in score:
        cnt += 1
        if j == 'X':
            cnt = 0
        print('cnt : ', cnt)
        answer += cnt
    print(answer)
