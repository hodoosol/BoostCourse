# 프로그래머스 _ 레벨 1 _ 소수 만들기
from itertools import combinations

def solution(nums) :
    nums = list(combinations(nums, 3))          # nums 중 세 개의 숫자를 조합, 순서 상관 없이
    temp = [sum(i) for i in nums]               # 조합한 원소들을 더해서 temp 리스트에 저장
                                                # 이 문제에서는 조합의 중복을 고려하기 때문에 list(set()) 하지않음
    cnt = 0                                     # 소수의 개수를 세는 cnt
    for i in temp :                             # 더해진 원소들 중
        for j in range(2, i) :                  # 2부터 원소 - 1까지 나누어 떨어진다면 break
            if i % j == 0 :
                break
        else :                                  # for - else 구문 사용 :
            cnt += 1                            # for문이 break된 적 없다면 소수이므로 cnt + 1
    return cnt                                  # cnt 리턴





# 프로그래머스 _ 레벨 1 _ 음양 더하기
def solution(absolutes, signs):

    for i in range(len(absolutes)) :
        if signs[i] == False :
            absolutes[i] *= -1

    answer = sum(absolutes)
    return answer



