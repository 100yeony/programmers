s = "()()"

def solution(s):
    x = 0
    for i in s:
        if i == '(':
            x += 1
        else:
            x -=1
        if x < 0:
            break

    # print(x==0)
    return x == 0

solution(s)
