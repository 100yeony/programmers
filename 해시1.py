from collections import Counter

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
final = []

def solution(participant, completion):
    result = Counter(participant).most_common()

    result_dict = {}
    for i in result:
        # result_dict = {i[0]:i[1]}
        result_dict[i[0]]=i[1]
    # print('first', result_dict)

    for i in completion:
        if i in result_dict:
            result_dict[i] -= 1
    # print('second', result_dict)

    for k,v in result_dict.items():
        if v != 0:
            return k

solution(participant, completion)
