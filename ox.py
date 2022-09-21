def solution(N):
    for i in range(N):
        case = input()
        answer = 0
        cnt = 0
        for j in case:
            cnt += 1
            if j == 'X':
                cnt = 0
            answer += cnt
        print(answer)

N = int(input())
solution(N)
