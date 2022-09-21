def solution(N, P):
    temp = 0
    answer = 0
    for i in range(N):
        if i == 0:
            temp = P[0]
        else:
            temp += P[i]
        answer += temp
    print(answer)

N = int(input())
P = sorted(map(int,input().split()),reverse=False)
solution(N, P)
