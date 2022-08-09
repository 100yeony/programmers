from collections import Counter

N = 5 #전체 스테이지 개수
stages = [2, 1, 2, 6, 2, 4, 3, 3] #이용자가 현재 멈춰있는 스테이지 번호
# result = [3,4,2,1,5]

# N=4
# stages=[4,4,4,4,4]
# result = [4,1,2,3]

def solution(N, stages):
    answer = []
    players = len(stages)

    # print('stages', stages)
    # print(Counter(stages))

    stages.sort()
    print(stages)


    failure = [min(stages)]
    # failure.append()

    for i in stages:
        failure.append()


    # hash = Counter(stages)
    # # hash = Dict(stages)
    # # print(sorted(hash.items()))
    # print(hash)
    # for k,v in hash.items():
    #     failure = v/players



    return answer

solution(N, stages)
