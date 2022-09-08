clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    # answer = 0

    # a = []
    # for i in clothes:
    #     a.append(i[::-1])

    # hash = dict(a)

    hash = dict(clothes)
    for i in clothes:
        hash = {i[1]:0}
    # hash = {x:y for x,y in x for x in clothes}







    print(hash)
    # return answer

solution(clothes)
