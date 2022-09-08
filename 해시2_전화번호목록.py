from collections import Counter

# phone_book = ["97674223", "1195524421", "119", "1191", "122"]
phone_book = ["119", "97674223", "1195524421"]

def solution(phone_book):
    # phone_book.sort()
    # str일때 접두어가 있다면 정렬로 앞 뒤 순서로 놓이게 됨 !!

    '''
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        # print(p1, p2)
        if p2.startswith(p1):
            # print('False')
            return False
    return True
    '''


    phone_book.sort()
    hash = {x:1 for x in phone_book}
    # print(hash)

    # for i in range(len(phone_book)-1):
    #     if phone_book[i] in hash:
    #         print(phone_book[i])

    for phone_number in phone_book:

        jubdoo = ""
        for number in phone_number:
            jubdoo += number
            # print(jubdoo)

            if jubdoo in hash and jubdoo!= phone_number:
                # print(jubdoo, 'False')
                # print('false')
                return False

    # print('true')
    return True

    #리스트 말고 딕셔너리로 만든 후 해시로 key 찾기, 그리고 인덱스로 비교

solution(phone_book)
