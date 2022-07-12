from collections import Counter

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
final = []

def solution(participant, completion):
    '''
    result = Counter(participant).most_common()

    result_dict = {}
    for i in result:
        result_dict[i[0]]=i[1]
    # print('first', result_dict)

    for i in completion:
        if i in result_dict:
            result_dict[i] -= 1
    # print('second', result_dict)

    for k,v in result_dict.items():
        if v != 0:
            return k
    '''

    '''
    다른 사람 풀이 : collection 객체로 리턴해서 빼기 연산이 가능
    '''
    result = Counter(participant) - Counter(completion)
    # print(result)
    return list(result.keys())[0]

solution(participant, completion)
