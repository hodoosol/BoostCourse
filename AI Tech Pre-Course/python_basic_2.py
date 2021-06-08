"""
2021.06.07

프로그래머스 파이썬을 파이썬답게
day 2

"""

"""
* i번째 원소와 i + 1번째 원소
<문제 설명>
숫자를 담은 리스트 mylist가 solution 함수의 파라미터로 주어집니다. 
solution 함수가 mylist의 i번째 원소와 
i+1번째 원소의 차를 담은 일차원 리스트에 차례로 담아 리턴하도록 코드를 작성해주세요.
단, 마지막에 있는 원소는 (마지막+1)번째의 원소와의 차를 구할 수 없으니, 이 값은 구하지 않습니다.

<제한 조건>
mylist의 길이는 1 이상 100 이하인 자연수입니다.
mylist의 원소는 1 이상 100 이하인 자연수입니다.

<예시>
mylist	                output
[83, 48, 13, 4, 71, 11]	[35, 35, 9, 67, 60]

<설명>
83과 48의 차는 35입니다.
48과 13의 차는 35입니다.
13과 4의 차는 9입니다.
4와 71의 차는 67입니다.
71과 11의 차는 60입니다.
따라서 [35, 35, 9, 67, 60]를 리턴합니다.

"""

# 내 답
def solution(mylist) :
    answer = []
    for i in range(len(mylist) - 1) :
        answer.append(abs(mylist[i] - mylist[i + 1]))
    return answer

# 모범 답안
def solution(mylist) :
    answer = []
    for num1, num2 in zip(mylist, mylist[1:]) :
        answer.append(abs(num1 - num2))
    return answer





"""
* 모든 멤버의 type 변환하기
<문제 설명>
문자열 리스트 mylist를 입력받아, 이 리스트를 정수형 리스트로 바꾼 값을 리턴하는 함수를 만들어주세요. 

<제한조건>
mylist의 길이는 100 이하인 자연수입니다.
mylist의 원소는 10진수 숫자로 표현할 수 있는 문자열입니다. 즉, 'as2' 와 같은 문자열은 들어있지 않습니다.

<예시>
input	            output
['1', '100', '33']	[1, 100, 33]

"""

# 내 답
def solution(mylist) :
    answer = []
    for i in mylist :
        answer.append(int(i))
    return answer

def solution2(mylist) :
    answer = list(map(int, mylist))
    return answer





"""
* map 함수 응용하기
<문제 설명>
정수를 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. 
solution 함수가 mylist 각 원소의 길이를 담은 리스트를 리턴하도록 빈칸을 완성해보세요.
hint) 이전 강의에서 배운 map 함수를 활용해보세요

<제한 조건>
mylist의 길이는 100 이하인 자연수입니다.
mylist 각 원소의 길이는 100 이하인 자연수입니다.

<예시>
input	                output
[[1], [2]]	            [1, 1]
[[1, 2], [3, 4], [5]]	[2, 2, 1]

"""

# 내 답
mylist = [[1, 2], [3, 4], [5]]
answer = list(map(len, mylist))
print(answer)





"""
* sequence 멤버를 하나로 이어붙이기
<문제 설명>
문자열 리스트 mylist를 입력받아, 
이 리스트의 원소를 모두 이어붙인 문자열을 리턴하는 함수, solution을 만들어주세요. 
예를 들어 mylist가 ['1', '100', '33'] 인 경우, solution 함수는 '110033'을 리턴하면 됩니다.

<제한 조건>
mylist의 길이는 100 이하인 자연수입니다.
mylist의 원소의 길이는 100 이하인 자연수입니다.

"""

# 내 답
def solution(mylist) :
    answer = ''.join(mylist)
    return answer

def solution2(mylist) :
    answer = ''
    for i in mylist :
        answer += i
    return answer





"""
* 삼각형 별 찍기
<문제 설명>
이 문제에는 표준 입력으로 정수 n이 주어집니다.
별(*) 문자를 이용해 높이가 n인 삼각형을 출력해보세요.

<제한 조건>
n은 100 이하인 자연수입니다.

<예시>
입력
3
출력
*
**
***

"""

# 내 답
n = int(input())
for i in range(1, n + 1) :
    print('*' * i)





"""
* 곱집합 (Cartesian product) 구하기 - product
itertools.product를 사용하면 for문을 사용하지 않고도 곱집합을 구할 수 있다.

"""

import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))





"""
* 2차원 리스트를 1차원 리스트로 만들기
<문제 설명>
문자열을 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. 
solution 함수가 mylist를 일차원 리스트로 만들어 리턴하도록 코드를 작성해주세요.

<제한 조건>
arr의 길이는 1 이상 100 이하인 자연수입니다.
arr 원소의 길이는 5를 넘지 않습니다.

<예시>
input	                           output
[[1], [2]]	                       [1, 2]
[['A', 'B'], ['X', 'Y'], ['1']]	   ['A', 'B', 'X' ,'Y', '1']

"""

# 내 답
def solution(mylist) :
    answer = []
    for i in mylist :
        answer += i
    return answer

# 모범 답안
answer2 = sum(mylist, [])





"""
* 순열과 조합
<문제 설명>
숫자를 담은 일차원 리스트, mylist에 대해 mylist의 원소로 이루어진 모든 순열을 
사전순으로 리턴하는 함수 solution을 완성해주세요.

<제한 조건>
mylist 의 길이는 1 이상 100 이하인 자연수입니다.

<예시>
mylist	       output
[2, 1]	       [[1, 2], [2, 1]]
[1, 2, 3]	   [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

"""

# 내 답
import itertools
def solution(mylist) :
    answer = sorted(list(itertools.permutations(mylist)))
    return answer

# 모범 답안 _ 3개의 원소로 수열 만들기
import itertools
print(list(map(''.join, itertools.permutations(mylist))))

# 모범 답안 _ 2개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(mylist, 2))))




