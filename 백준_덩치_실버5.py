
# def solution(N):
'''
    arr = list()
    answer = list()
    # for i in range(N):
    #     xy = list(map(int,input().split()))
    #     xy.append(i+1)
    #     arr.append(xy)
    # # print(arr)
    #
    # sort_x = sorted(arr, key=lambda x: x[0], reverse=True)
    # sort_y = sorted(arr, key=lambda x: x[1], reverse=True)
    # print(sort_x)
    # print(sort_y)
    #
    # for i in range(N):
    #     if sort_x[i] != sort_y[i]:
    #
    #     else:
    #         sort_y[i].append(i+1)
    #
    # print(sort_y)

    x = list()
    y = list()
    xy = list()
    for i in range(N):
        x1,y1 = list(map(int,input().split()))
        x.append([x1, i+1])
        y.append([y1, i+1])
        xy.append([x1,y1,i+1])
    print('x', x)
    print('y', y)
    print('xy', xy)

    sort_x = sorted(x, reverse=True)
    sort_y = sorted(y, reverse=True)

    print('sort_x', sort_x)
    print('sort_y', sort_y)
    for i in range(N):
        if sort_x[i][1]==sort_y[i][1]:
            answer.append(i+1)
        else:
            answer.append(2)
    print('answer', answer)

N = int(input())
solution(N)
    '''
num_student = int(input())
student_list = []

for _ in range(num_student):
    weight, height = map(int, input().split())
    student_list.append((weight, height))

for i in student_list:
    rank = 1
    print('i', i)
    for j in student_list:
        print('j', j)
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    # print(rank, end = " ")
