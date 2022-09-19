# total = 0
# for tester in A:
#     temp1 = tester-B
#     if tester < 0:
#         total += 2
#         continue
#     else:
#         if temp1 < C:
#             total += 2
#         else:
#             total += (temp1//C + 2)
#         continue
#
# print(total)

def solution():
    answer = 0

    for i in range(N):
        if arr[i] > 0:
            arr[i] -= Master
            answer += 1
        if arr[i] > 0:
            answer += int(arr[i]/Sub)
            if arr[i] % Sub != 0:
                answer += 1
    return answer

N = int(input())
arr = list(map(int,input().split()))
Master, Sub = map(int,input().split( ))
print(solution())
