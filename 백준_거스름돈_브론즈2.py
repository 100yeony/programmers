def solution(price):
    money = 1000 - price
    answer = 0
    arr = [500, 100, 50, 10, 5, 1]

    for i in arr:
        cnt = 0
        if money >= i:
            cnt += money // i
            money -= cnt*i
        answer += cnt
        if money <= 0:
            break
    print(answer)

price = int(input())
solution(price)
