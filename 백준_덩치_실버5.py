def solution(N):
    arr = list()
    for i in range(N):
        xy = tuple(map(int,input().split()))
        arr.append(xy)

    # for i in arr:
        # print(i[0], type(i))
    temp = sorted(arr, key=lambda x: x[0] for x in arr)
    print(temp)


N = int(input())
solution(N)
