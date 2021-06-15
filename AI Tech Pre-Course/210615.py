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





# 프로그래머스 _ 레벨 1 _ 체육복
def solution(n, lost, reserve) :
    answer = n - len(lost)                        # 현재 체육복이 있는 학생 수
    lost = sorted(lost)                           # lost와 reserve 오름차순 정렬하기
    reserve = sorted(reserve)
    temp = list(set(lost).intersection(reserve))  # lost와 reserve의 교집합을 temp에 저장
                                                  # == 체육복을 도난당했지만 여분이 있는 학생
    for i in temp:
        lost.remove(i)                            # 그 학생을 lost와 reserve 리스트에서 삭제
        reserve.remove(i)
        answer += 1                               # 체육복이 있으므로 answer + 1

    for i in reserve:
        if i - 1 in lost:                         # 여분이 있는 학생의 앞번호 학생이 도난당했다면
            answer += 1                           # 체육복을 빌려주고, 리스트에서 삭제
            lost.remove(i - 1)
        elif i + 1 in lost:                       # 여분이 있는 학생의 뒷번호 학생이 도난당했다면
            answer += 1                           # 체육복을 빌려주고, 리스트에서 삭제
            lost.remove(i + 1)

    return answer                                 # 체육복이 있는 학생 수 반환
