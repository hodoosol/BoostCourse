"""
2021.06.03 목요일

[AI Tech Pre-course] 인공지능(AI) 기초 다지기

Chapter1. 파이썬 기초
3. 파이썬 기초 문법 2

"""


"""
1) Python Data Structure
* 데이터 구조 생각해보기
- 전화번호부 정보는 어떻게 저장하면 좋을까 ?
- 은행 번호표 정보는 ?
- 서적 정보는 ?
- 창고에 쌓인 수화물의 위치를 역순으로 찾으려면 ?



2) 스택과 큐
* Stack
- 나중에 넣은 데이터를 먼저 반환하도록 설계된 메모리 구조
- Last In First Out (LIFO)
- 데이터의 입력을 push, 출력을 pop이라고 한다.
- 리스트를 사용하여 스택의 구조를 구현 가능하다.
- push = append(), pop = pop()

pop()이라는 함수는 return이 있으면서도 리스트의 값을 바꾸는 함수이다.

* Queue
- 먼저 넣은 데이터를 먼저 반환하도록 설계된 메모리 구조
- First In First Out (FIFO)
- 데이터의 입력을 put, 출력을 get이라고 한다.
- stack과 반대되는 경우
- 큐도 리스트를 사용하여 구조를 구현할 수 있다.
- put = append(), get = pop(0)



3) 튜플과 집합
* tuple
- 값의 변경이 불가능한 리스트
- 선언시 () 를 사용한다.
- 리스트의 연산, 인덱싱, 슬라이싱 등을 동일하게 사용한다.

- 프로그램을 작동하는 동안 변경되지 않을 or 변경되면 안되는 데이터의 저장을 위해 사용한다.
  ex) 학번, 이름, 우편번호 등
- 함수의 반환 값 등 사용자의 실수에 의한 에러를 사전에 방지한다.

- 값이 하나인 튜플은 반드시 , 를 붙여야 한다.
ex)
t = (1)
type(t) -> int

t = (1, )
type(t) -> tuple



* 집합 (set)
- 값을 순서 없이 저장, 중복을 불허하는 자료형
- set 객체 선언을 이용하여 객체 생성
- 수학에서 활용하는 다양한 집합 연산 가능 (합, 교, 차집합 등)



4) 사전
- 데이터를 저장할 때, 구분 지을수 있는 값을 함께 저장
  ex) 주민등록 번호, 제품 모델 번호
- 구분을 위한 데이터 고유 값을 Identifier 또는 Key라고 한다.
- Key 값을 활용하여, 데이터 값(Value)을 관리함
- 다른 언어에서는 hash table이라고 하기도 함



5) collection 모듈
- list, tuple, dict 에 대한 python built-in 확장 자료 모듈
- 편의성, 실행 효율 등을 사용자에게 제공한다.

from collections import deque
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import namedtuple

* deque
- rotate, reverse 등 linked list의 특성을 지원한다.
- 기존 list 형태의 함수를 모두 지원한다.
- 기존 list 보다 효율적인 자료구조와 메모리 구조 제공 -> 처리 속도 향상

* OrderedDict
- Dict와 달리 데이터를 입력한 순서대로 반환한다.
- but, dict도 python3.6 부터 입력한 순서를 보장하여 출력하게 되었다.

* defaultdict
- dict type의 값에 기본 값을 지정, 신규값 생성시 사용하는 방법

from collections import defaultdict
# 디폴트 딕셔너리 생성
d = defaultdict(object)
# 디폴트 값을 0으로 설정함
d = defaultdict(lambda : 0)
print(d['first']) -> 0 출력된다.

- 하나의 지문에 각 단어들이 몇 개나 있는지 세고 싶을 경우 ?
  Text-mining 접근법 (vector space model)
  
* Counter
- 시퀀스 타입의 데이터 원소들의 개수를 dict로 반환한다.
ex)
from collections import Counter
ball_or_strike = ['b', 's', 's', 's', 's', 'b', 'b']
c = Counter(ball_or_strike)
print(c) -> Counter({'b' : 3, 's' : 4})

* namedtuple
- tuple 형태로 data 구조체를 저장하는 방법
- 저장되는 data의 변수를 사전에 지정해서 저장한다.



"""

