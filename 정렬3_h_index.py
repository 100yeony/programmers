import math

citations = [3, 0, 6, 1, 5, 4, 18, 20, 21, 22, 23, 24, 7]
# citations = [4,4,4]

def solution(citations):
    '''
    #나의 풀이
    paper = len(citations)
    citations.sort()

    # print('len', len(citations), len(citations)%2)
    if len(citations)%2 != 0:
        # print('홀수')
        print(citations[int(citations.index(citations[-1])/2)])
        # return citations[int(citations.index(citations[-1])/2)]
    else:
        # print('짝수')
        print(citations[math.trunc(citations.index(citations[-1])/2)])
        # return citations[math.trunc(citations.index(citations[-1])/2)]
    '''


    citations.sort(reverse=True)
    # print(citations)
    for i in range(len(citations)):
        if citations[i] <= i:
            # print(i)
            return i

    # print(len(citations))
    return len(citations)
    # return answer

solution(citations)
