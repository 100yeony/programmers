array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

#시퀀스 슬라이싱[이상:미만]
'''
# 나의 풀이

def solution(array, commands):
    # print(commands[0][1])
    answer = []
    for i in commands:
        ii = i[0]
        jj = i[1]
        kk = i[2]
        # print('i',ii, 'j',jj, 'k',kk)

        temp = array[ii-1:jj]
        # print("temp", temp)
        temp.sort()
        # print(temp[kk-1])
        answer.append(temp[kk-1])
        # print(answer[kk-1])
    # print(answer)
    return answer
solution(array, commands)
'''

# '''
# 다른사람 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1],commands))
    # print(list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands)))
    # return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]]-1), commands)

solution(array, commands)
# '''
