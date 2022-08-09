# numbers = [3, 30, 34, 5, 9]
numbers = [6, 10, 2]

'''
#나의 풀이

def solution(numbers):
    answer = sorted(numbers, key=lambda x:str(x)[0], reverse=True)
    # print(answer)

    temp = []
    idx = 0
    final=''
    for p1, p2 in zip(answer, answer[1:]):
        # print('/', p1, p2)

        if str(p1)[0]==str(p2)[0]:
            idx = answer.index(p1)
            temp.append(p1)
            temp.append(p2)

            # print('?', p1, p2)
            if len(str(p1))<len(str(p2)):
                if str(p1)[0]<str(p2)[1]:
                    answer[answer.index(p2)],answer[answer.index(p1)] = answer[answer.index(p1)],answer[answer.index(p2)]

            elif len(str(p1))==len(str(p2)):
                if str(p1)[1]<str(p2)[1]:
                    # print(answer)
                    answer[answer.index(p2)],answer[answer.index(p1)] = answer[answer.index(p1)],answer[answer.index(p2)]

            answer2 = answer[0:idx-1]
            temp = list(set(temp))
            # print(answer)
            # print('answer2',answer2)
            answer3 = answer2 + temp

            for i in answer3:
                final+=str(i)
            # print('final',final)


        else:
            # print(answer)
            for i in answer:
                final+=str(i)
            # print(final)

    return final
    '''

#남의 풀이
def solution(numbers):
    if sum(numbers)==0:
        return '0'

    answer = list(map(str, numbers))
    # print(answer)
    answer = sorted(answer, key=lambda x:x*3, reverse=True)
    # print(answer)
    final = str(int(''.join(answer)))
    # print(final)
    return final


solution(numbers)
