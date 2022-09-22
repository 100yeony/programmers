from itertools import combinations
def solution(N, M, number):
    a = sorted(list(map(sum,combinations(number,3))), reverse=True)
    for i in a:
        if i <= M:
            print(i)
            break

N, M = map(int,input().split())
number = list(map(int,input().split()))
solution(N,M, number)
