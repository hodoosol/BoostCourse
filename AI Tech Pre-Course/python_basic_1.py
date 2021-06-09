"""
2021.06.06 일요일

프로그래머스 파이썬을 파이썬답게

"""


"""
* 수강 전에 이 문제를 풀어보세요.
정수를 담은 이차원 리스트, mylist 가 solution 함수의 파라미터로 주어집니다. 
mylist에 들은 각 원소의 길이를 담은 리스트를 리턴하도록 solution 함수를 작성해주세요.

<제한 조건>
mylist의 길이는 100 이하인 자연수입니다.
mylist 각 원소의 길이는 100 이하인 자연수입니다.

<예시>
input	                output
[[1], [2]]	            [1,1]
[[1, 2], [3, 4], [5]]	[2,2,1]

"""

def solution(mylist) :
    answer = []
    for i in mylist :
        answer.append(len(i))
    return answer


# 이 코드가 더 파이썬스럽다.
def solution_1(mylist) :
    return list(map(len, mylist))





"""
* 몫과 나머지
숫자 a, b가 주어졌을 때 a를 b로 나눈 몫과 a를 b로 나눈 나머지를 공백으로 구분해 출력해보세요.

<입력 설명>
입력으로는 공백으로 구분된 숫자가 두 개 주어집니다.
첫 번째 숫자는 a를 나타내며, 두 번째 숫자는 b를 나타냅니다.

<출력 설명>
a를 b로 나눈 몫과 a를 b로 나눈 나머지를 공백으로 구분해 출력하세요.

<제한 조건>
a와 b는 자연수입니다.

"""

# 내 답
a, b = map(int, input().split())
print(a // b, a % b)

# 모범 답안
a, b = map(int, input().strip().split(' '))
print(*divmod(a, b))





"""
* n진법으로 표기된 string을 10진법 숫자로 변환하기
<문제 설명>
base 진법으로 표기된 숫자를 10진법 숫자 출력해보세요.

<입력 설명>
입력으로는 공백으로 구분된 숫자가 두 개 주어집니다.
첫 번째 숫자는 num을 나타내며, 두 번째 숫자는 base를 나타냅니다.

<출력 설명>
base 진법으로 표기된 num을 10진법 숫자로 출력해보세요.

<제한 조건>
base는 10 이하인 자연수입니다.
num은 3000 이하인 자연수입니다.

<예시>
input	output
12 3	5
444 5	124

<입출력 예 설명>
입출력 예 1
3진법으로 표기된 12는 10진법으로 표현하면 5입니다. ( 1*3 + 2 )

입출력 예 2
5진법으로 표기된 444는 10진법으로 표현하면 124입니다. ( 4*5*5 + 4*5 + 4 )


"""

# 내 답
n, b = map(int, input().split())
n = list(str(n))
ex = len(n) - 1
answer = 0
for i in range(ex + 1) :
    answer += int(n[i]) * (b ** (ex - i))
print(answer)

# 모범 답안
n, b = map(int, input().split())
answer = int(str(n), b)
print(answer)





"""
* 문자열 정렬하기
<문제 설명>
문자열 s와 자연수 n이 입력으로 주어집니다. 문자열 s를 좌측 / 가운데 / 우측 정렬한 길이 n인 문자열을 한 줄씩 프린트해보세요.

<제한조건>
s의 길이는 n보다 작습니다.
(n - s의 길이)는 짝수입니다.
s는 알파벳과 숫자로만 이루어져 있으며, 공백 문자가 포함되어있지 않습니다.

입력 예
abc 7
출력 예
abc      
   abc   
      abc

"""

# 내 답  ==  모범 답안
s, n = input().split()
n = int(n)
print(s.ljust(n))
print(s.center(n))
print(s.rjust(n))





"""
* 알파벳 출력하기
<문제 설명>
입력으로 0이 주어지면 영문 소문자 알파벳을, 입력으로 1이 주어지면 영문 대문자 알파벳을 사전 순으로 출력하는 코드를 짜세요.

<예시 1>
입력
0

출력
abcd...(중간생략)..xyz

<예시 2>
입력
1

출력
ABCD...(중간생략)..XYZ

"""

# 내 답
if int(input()) == 0 :
    for i in range(97, 123) :
        print(chr(i), end='')
else :
    for i in range(65, 91) :
        print(chr(i), end='')

# 모범 답안
import string
if int(input()) == 0 :
    print(string.ascii_lowercase)
else :
    print(string.ascii_uppercase)





"""
* 2차원 리스트 뒤집기
<문제 설명>
다음을 만족하는 함수, solution을 완성해주세요.

solution 함수는 이차원 리스트, mylist를 인자로 받습니다
solution 함수는 mylist 원소의 행과 열을 뒤집은 한 값을 리턴해야합니다.
예를 들어 mylist [[1, 2, 3], [4, 5, 6], [7, 8, 9]]가 주어진 경우, 
solution 함수는 [[1, 4, 7], [2, 5, 8], [3, 6, 9]] 을 리턴하면 됩니다.

<제한 조건>
mylist의 원소의 길이는 모두 같습니다.
mylist의 길이는 mylist[0]의 길이와 같습니다.
각 리스트의 길이는 100 이하인 자연수입니다.

"""

# 내 답
def solution(mylist) :
    l = len(mylist)
    answer = []
    for i in range(l) :
        temp = []
        for j in range(l) :
            temp.append(mylist[j][i])
        answer.append(temp)
    return answer

# 모범 답안
def solution(mylist) :
    answer = list(map(list, zip(*mylist)))
    return answer

def solution(mylist) :
    answer = [list(i) for i in zip(*mylist)]
    return answer



