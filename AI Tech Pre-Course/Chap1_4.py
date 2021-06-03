"""
2021.06.03 목요일

[AI Tech Pre-course] 인공지능(AI) 기초 다지기

Chapter1. 파이썬 기초
4. Pythonic Code

"""



"""
** 강의에 더 자세한 용법과 그 예시가 실려있었지만 기본적인 것만 필기했다.
1) Pythonic Code
- 파이썬 스타일의 코딩 기법
- 파이썬 특유의 문법을 활용하여 효율적으로 코드를 표현함
- but, 더이상 파이썬 특유는 아님, 많은 언어들이 서로의 장점을 채용 중
- 고급 코드를 작성할 수록 더 많이 필요해진다.

* 여러 단어들을 하나로 붙일 때
colors = ['red', 'blue']
result = ''
for s in colors :
    result += s
    
위 코드보다 아래의 코드가 파이써닉하다.
colors = ['red', 'blue']
result = ''.join(colors)

- split, join, list comprehension, enumerate, zip, lambda, map, reduce, generator, asterisk ...

* 왜 파이써닉 해야하는가 ?
- 다른 사람의 코드에 대한 이해도가 올라간다.
- 효율적이다.

1. split & join
- string type의 값을 기준값으로 나누어 list 형태로 변환
ex)
items = 'zero one two three'
x = items.split()
x = ['zero', 'one', 'two', 'three']

y = '-'.join(x)
y = 'zero-one-two-three'



2. list comprehension
- 기존 list를 사용하여 간단하게 다른 list를 만드는 기법
- 포괄적인 list, 포함되는 리스트라는 의미로 사용된다.
- 일반적으로 for + append 보다 빠르다.

ex)
result = [i for i in range(10)]
result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result = [i for i in range(10) if i % 2 == 0]
result = [0, 2, 4, 6, 8]



3. enumerate & zip
* enumerate
- list의 요소를 추출할 때 번호를 붙여서 추출한다.
ex)
for i, v in enumerate(['tic', 'tac', 'toe']) :
    print(i, v)
->     
0 tic
1 tac
2 toe 인덱스와 요소가 함께 출력된다.

* 중복되는 값 없애기
nums = []
print(list(set(nums))

* zip
- 두 개의 list의 값을 병렬적으로 추출한다.
ex)
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

print([[a, b] for a, b, in zip(alist, blist)])
-> [['a1', 'b1'], ['a2', 'b2'], ['a3', 'b3]]



4. lambda 함수
- 함수의 이름 없이 함수처럼 쓸 수 있는 익명의 함수
ex)
f = (lambda x, y : x + y)
f(10, 50) -> 60



5. map 함수
- 두 개 이상의 list에서 적용, 함수에 값을 전달하고 반환받을 수 있다.
ex)
def f(x) :
    return x + 5
ex = [1, 2, 3, 4, 5]    
result = list(map(f, ex))
print(result) -> [6, 7, 8, 9, 10]



6. reduce 함수
- map과 달리 list에 똑같은 함수를 적용해서 통합
ex)
from functools import reduce
result = reduce(lambda x, y : x + y, [1, 2, 3, 4, 5]))
-> 1과 2를 적용한 값 = 3을 그 다음 원소인 3과 함수에 적용하여 6을 얻고....
f(1, 2) = 3
f(3, 3) = 6
f(6, 4) = 10
f(10, 5) = 15 가 되는 것이다.



7. iterable objects
- 시퀀스형 자료형에서 데이터를 순서대로 추출하는 object
- 내부적 구현으로 __iter__와 __next__가 사용된다.
- iter(), next() 함수로 iterable 객체를 iterator object로 사용한다.

ex)
city = ['seoul', 'jeju']
memory_address = iter(city) -> city의 메모리 주소를 가져온다.
next(memory_address) -> 'seoul'
next(memory_address) -> 'jeju'



8. generator
- iterable object를 특수한 형태로 다루어 준다.
- element가 사용되는 시점에 값을 메모리에 반환한다.
- yield를 사용해 한 번에 하나의 element만 반환한다.

ex)
def general_list(value) :
    result = []
    for i in range(value) :
        result.append(i)
    return result
    
general_list(10) -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

import sys
result = general_list(10)
sys.getsizeof(result) -> 520

def generator_list(value) :
    result = []
    for i in range(value) :
        yield i -> 한꺼번에 메모리에 올려두지 않고, 값이 들어올 때 마다 던져준다.

for a in generator_list(10) :
    print(a)
-> 0 1 2 3 4 5 6 7 8 9

result = generator_list(10)
sys.getsizeof(result) -> 112 , 현저히 작은 메모리


* list 타입의 데이터를 반환해주는 함수는 generator로 만드는 것이 좋다.
* 큰 데이터를 처리할 때는 generator expression 을 고려해야 한다.
* 파일 데이터를 처리할 때도 generator를 쓰자.



9. function passing arguments
* keyword arguments
- 함수에 입력되는 파라미터의 변수명을 사용하여 argument를 넘긴다.
ex)
def print_something(my_name, your_name) :
    print('hello {0}, my name is {1}'.format(your_name, my_name))
    
print_something('dasol', 'buddy')
print(your_name = 'buddy', my_name = 'dasol)

* default arguments
- 파라미터의 기본 값을 사용, 입력하지 않은 경우 기본값을 출력한다.
ex)
def print_something_2(my_name, your_name = 'buddy') :
    print('hello {0}, my name is {1}'.format(your_name, my_name))    

print_something_2('dasol', 'buddy')
print_something_2('dasol') -> 둘의 결과는 같다.



10. variable-length asterisk
* 가변인자 using asterisk
- 개수가 정해지지 않은 변수를 함수의 파라미터로 사용하는 방법이다.
- 가변인자는 일반적으로 *args를 변수명으로 사용한다.
- 기존 파라미터 이후에 나오는 값을 tuple로 저장한다.

ex)
def asterisk_test(a, b, *args) :
    return a + b + sum(args)
    
a = asterisk_test(1, 2, 3, 4, 5)
print(a) -> 10

* 키워드 가변인자
- 파라미터 이름을 따로 지정하지 않고 입력하는 방법이다.

ex)
def kwargs_test(**kwargs) :
    print(kwargs)

kwargs_test(first = 3, second = 4, third = 5)
-> {'first' : 3, 'second' : 4, 'third' : 5}   dict 타입으로 저장한다.


* = asterisk
흔히 알고있는 *를 의미한다.
단순 곱셈, 제곱 연산, 가변 인자 활용 등 다양하게 사용된다.
tuple, dict 등 자료형에 들어가 있는 값을 unpacking 한다.
함수의 입력값, zip 등에 유용하게 사용할 수 있다.



"""


