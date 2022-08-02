# from collections import Counter
# from itertools import combinations

nums = [3,3,3,2,2,4,5,6,6,7,8,8,9]

def solution(nums):
    # 최대 골라야 할 마리 수가 정해져 있기 때문에 중복 제거한 값과 선택해야 하는 수 중 더 작은 값 선택
    choose = int(len(nums) / 2)
    set_nums = len(set(nums))
    answer = min(choose, set_nums)
    return answer

solution(nums)
