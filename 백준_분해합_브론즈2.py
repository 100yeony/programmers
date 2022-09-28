from itertools import combinations
kids = list()
for i in range(9):
    height = int(input())
    kids.append(height)

kids.sort()
kids_7 = list(combinations(kids,7))
answer = list()
for i in kids_7:
    if sum(i) == 100:
        answer.append(i)

for i in answer[0]:
    print(i)
