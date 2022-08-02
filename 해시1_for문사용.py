# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]
from collections import Counter

participant = []
completion = []

def solution(participant, completion):

    # 첫번째 풀이: for문 이용
    # 결과 : 효율성 0으로 실패
    # for i in completion:
    #     if i in participant:
    #             participant.remove(i)
    # return participant[0]
    # print('?')

    # 두번째 풀이: dictionary 타입 이용

    p_dict = {string: 0 for string in participant}

    for i in completion:
        if i in p_dict:
            p_dict[i] = p_dict[i] + 1
    # print(p_dict)

    for k,v in p_dict.items():
        # print(k,v)
        if v == 0:
            return k


solution(participant, completion)
