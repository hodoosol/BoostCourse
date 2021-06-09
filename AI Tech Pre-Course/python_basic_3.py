"""
2021.06.09

프로그래머스 파이썬을 파이썬답게
day 3 _ 완

"""


"""
* 가장 많이 등장하는 알파벳 찾기
<문제 설명>
이 문제에는 표준 입력으로 문자열, mystr이 주어집니다.
mystr에서 가장 많이 등장하는 알파벳만을 사전 순으로 출력하는 코드를 작성해주세요.

<제한 조건>
mystr의 원소는 알파벳 소문자로만 주어집니다.
mystr의 길이는 1 이상 100 이하입니다.

<예시>
input	     output
'aab'	     'a'
'dfdefdgf' 	 'df'
'bbaa'	     'ab'

"""

# 내 답 _ 오랜만에 하려니까 조금 힘드넹 ... 딕셔너리의 키와 밸류 다루는 법이 헷갈린다.
import collections

mystr = sorted(input())
cnt = collections.Counter(mystr)
M = max(list(cnt.values()))

for i in range(97, 123) :
    if cnt[chr(i)] == M :
        print(chr(i), end='')





"""
* for 문과 if 문을 한 번에
<문제 설명>
정수를 담은 리스트 mylist를 입력받아, 
이 리스트의 원소 중 짝수인 값만을 제곱해 담은 새 리스트를 리턴하는 solution함수를 완성해주세요. 

예를 들어, 
[3, 2, 6, 7]이 주어진 경우

3은 홀수이므로 무시합니다.
2는 짝수이므로 제곱합니다.
6은 짝수이므로 제곱합니다.
7은 홀수이므로 무시합니다.

따라서 2의 제곱과 6의 제곱을 담은 리스트인 [4, 36]을 리턴해야합니다.

<제한 조건>
mylist는 길이가 100이하인 배열입니다.
mylist의 원소는 1이상 100 이하인 정수입니다.

"""

# 내 답
def solution(mylist) :
    answer = []
    for i in mylist :
        if i % 2 == 0 :
            answer.append(i ** 2)
    return answer

# 모범 답안 _ list comprehension
def solution(mylist) :
    answer = [n ** 2 for n in mylist if n % 2 == 0]
    return answer





"""
* flag OR for - else
<문제 설명>
본 문제에서는 자연수 5개가 주어집니다.
숫자를 차례로 곱해 나온 수가 제곱수1가 되면 found를 출력하고
모든 수를 곱해도 제곱수가 나오지 않았다면 not found를 출력하는
코드를 작성해주세요.

<예시 >
입력
2
4
2
5
1

출력
found

"""

# 내 답
a = 1
for i in range(5) :
    a *= int(input())
    temp = a ** 0.5
    if temp == int(temp) :
        print('found')
        break
    if i == 4 :
        print('not found')





"""
* 두 변수의 값 바꾸기 - swap
파이썬에서는 다음과 같이 한 줄로 두 값을 바꿔치기할 수 있습니다.

a = 3
b = 'abc'

a, b = b, a 
참 쉽죠?

"""





# 이진 탐색하기 - binary search

#  반복문 사용
def bisect(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect(mylist, 3))


#  bisect 사용
import bisect

mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))





"""
* 가장 큰 수, inf
파이썬이 제공하는 inf 를 사용해보세요. 
inf는 어떤 숫자와 비교해도 무조건 크다고 판정됩니다.

min_val = float('inf')
min_val > 10000000000

inf에는 음수 기호를 붙이는 것도 가능합니다.

max_val = float('-inf')

"""




