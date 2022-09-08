arr = [1,1,3,3,0,1,1]

def solution(arr):
    answer = []
    #나의 풀이
    '''
    for i in arr:
        if len(answer) == 0:
            answer.append(i)
        elif answer[-1] != i:
            answer.append(i)
    '''
    #다른사람 풀이
    for i in arr:
        if answer[-1:]==[i]:
            continue
        answer.append(i)
    return answer

solution(arr)
