answers = [1,2,3,4,5]
p1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
p2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

def solution(answers):

    for i, j in enumerate(answers):
        print(i,j)



solution(answers)
