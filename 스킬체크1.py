n = 123

def solution(n):
    # answer = 0
    nn = list(str(n))
    # print(nn)
    sum=0
    for i in nn:
        sum += int(i)
    # print(sum)
    return sum


    # print(list(map(lambda x:x+x, n)))


    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')

    # return answer

solution(n)
