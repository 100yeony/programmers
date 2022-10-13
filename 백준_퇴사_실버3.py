N = int(input())
arr = list()
for i in range(N):
    arr.append(list(map(int,input().split())))

# idx = 0
temp = arr[0]
answer = temp[1]



for idx in range(N):
    T = temp[0]
    P = temp[1]
    x = arr.index(temp)+T
    # print(x, arr[idx][0])

    if idx != 0 and x == idx and idx+T <= N:
        temp = arr[idx]
        print(x, idx, temp, temp[1])
        # print(arr[idx][1])
        answer += temp[1]
    else:
        print('?', x, idx)
        continue

print(answer)
