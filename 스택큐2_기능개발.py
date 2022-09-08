import math

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

def solution(progresses, speeds):
    answer = []
    answer2 = []
    for p, s in zip(progresses, speeds):
        day = math.ceil((100 - p)/s)
        # print(day)
        answer.append(day)

    print(answer)
    

    '''

    for i in answer2:
        if len(answer3)== 0:
            answer3.append(i)
        elif answer3[-1:] >= [i]:
            answer3.append(i)
        elif answer3[-1:] < [i]:
            answer4.append(len(answer3))
            answer3.clear()
            answer3.append(i)
    answer4.append(len(answer3))
    '''
    # print(answer4)
    # return answer4

solution(progresses, speeds)
