"""
2021.06.02 수요일

[AI Tech Pre-course] 인공지능(AI) 기초 다지기

Chapter1. 파이썬 기초
2. 파이썬 기초 문법

"""



"""
1) Variables
 1. Variables
- 가장 기초적인 프로그래밍 문법 개념
- 값을 저장하는 장소, 선언되는 순간 메모리 특정 영역에 물리적인 공간이 할당된다.
- 데이터(값)을 저장하기 위한 메모리 공간의 프로그래밍 상 이름
- 변수는 메모리 주소를 가지고 있고, 변수에 들어가는 값은 메모리 주소에 할당된다.

name = 'dasol'의 의미는 ? name에 'dasol'을 넣어라.

* 컴퓨터의 구조 - 폰 노이만 아키텍처
폰 노이만 아키텍처에서는 사용자가 컴퓨터에 값을 입력하거나 프로그램을 실행할 경우,
그 정보를 먼저 메모리에 저장하고
CPU가 순차적으로 그 정보를 해석하고 계산하여 사용자에게 결과값을 전달한다.



 2. Basic Operation
data type : integer, float, string, boolean

* dynamic typing
- 코드 실행시점에 데이터의 type을 결정하는 방법



 3. Operator & Operand
연산자 : + - * / ** % //
피연산자 : 연산자가 적용되는 숫자



 4. list
- 시퀀스 자료형, 여러 데이터들의 집합
- int, float 같은 다양한 데이터 타입 포함

* 인덱싱
- list에 있는 모든 값들은 주소를 가짐, 이 주소를 사용하여 할당된 값을 호출하는 방법

* a = [1, 2, 3, 4, 5]
b = [2, 3, 4] 일 때,
a = b 를 실행하면
a = [1, 2, 5] 로 a의 값을 바꿨을 때 b의 값도 같이 바뀌게 된다.
따라서, a의 모든 원소를 b에 복사하고 싶을 때는
b = a[:] 를 사용하면 된다.

* 패킹
t = [1, 2, 3]
a, b, c = t
a = 1
b = 2
c = 3
이렇게 하나의 변수 t에 여러 개의 데이터를 넣는 것을 패킹이라고 하고,
한 변수의 데이터를 차례로 풀어서 각각의 변수에 할당하는 것을 언패킹이라고 한다.

* 2차원 리스트
- 리스트 안에 리스트를 만들어 행렬(matrix)를 생성
kor = [100]
eng = [89]
math = [99]
midterm = [kor, eng, math]
midterm = [[100], [89], [99]]

2차원 리스트를 복사할 때, 1차원 리스트와 마찬가지로 [:] 구문을 사용하면 ? X
midterm_copy = midterm[:]
midterm[0][0] = 70

midterm = [[70], [89], [99]]
midterm_copy = = [[70], [89], [99]]  midterm의 값을 바꿔면 함께 바뀌게 된다.

따라서, copy 모듈을 사용해야 한다.
import copy
midterm_copy2 = copy.deepcopy(midterm)





2) Function and Console I/O
 1. function
- 어떤 일을 수행하는 코드의 덩어리, 코드를 논리적인 단위로 분리
- 반복적인 수행을 1회만 작성 후 호출한다.
- 캡슐화 : 인터페이스만 알면 타인의 코드 사용 가능

def 함수 이름 (parameter, ... , ) :
    수행문 #1(statements)
    수행문 #2(statements)
    return 반환값
    
    
def calculate_rectangle_area(x, y)
    result = x * y
    

* 파라미터 유무, 반환 값 유무에 따라 함수의 형태가 다름
parameter = 함수의 입력 값 인터페이스
argument = 실제 파라미터에 대입된 값

                   파라미터 없음                       파라미터 존재
반환 값 없음     함수 내의 수행문만 수행           파라미터를 사용, 수행문만 수행
반환 값 존재     파라미터 없이, 수행문 수행 후     파라미터를 사용하여 수행문 수행 후
                결과값 반환                        결과값 반환
                
ex)
def f(x) :
    print(x + 10)
    
리턴 값이 없는 함수이다.
f(10)을 출력해보면 20이 나온다.
그러나 c = f(10), print(c)를 하면 None이 출력된다.
리턴 값이 없어 c에 함수의 값이 할당되지 않았기 때문이다.

ex)
def f(x) :
    return x + 10
    
c = f(10)
print(c) -> 20 리턴값이 있긴 함수이기 때문에 변수 c에 함수의 값이 잘 할당되었다.

비슷하게, sorted()와 sort()도 차이가 난다.
sorted(리스트명)은 리스트의 값을 정렬하여 출력만 하고 재할당은 하지 않는 함수이고,
리스트명.sort()은 리스트의 값을 정렬하여 할당만 하고 출력은 하지 않는 함수이다.



 2. Console I/O
input() 함수로 입력 받는다.

* print문을 사용해서 formatting 하기
(1) %format - '%datatype' %(variable)
ex) print('%s %s' % ('one', 'two'))
    
(2) format 함수
ex) print('{} {}'.format('one', 'two'))

(3) fstring
- python 3.6 이후, PEP498에 근거한 formatting 기법
ex) 
name = 'dasol'
age = 26
print(f'Hello, {name}. You are {age}.')
 -> Hello, dasol. You are 26. 

+) padding
- 여유 공간을 지정하여 글자배열 + 소수점 자릿수를 맞추기
ex)
print(f'{name : 20}') -> dasol
print(f'{name : >20}') ->             dasol
print(f'{name : *<20}') -> dasol***********
print(f'{name : *>20}') -> ***********dasol
print(f'{name : *^20}') -> ******dasol******

+) naming
- 해당 표시할 내용을 변수로 표시하여 입력
ex) print('product : %(name)10s, Price per unit : %(price)10.5f.' % {'name' : 'Dasol', 'price' : 5.243})





3) Conditionals and Loops
* 조건문
if - else
if - elif - else

* 반복문
for
while

* debugging
- 코드의 오류를 발견하여 수정하는 과정, 오류의 원인을 알고 해결책을 찾아야 함
- 문법적 에러 : 에러 메세지 분석
- 논리적 에러 : 테스트 필수





4) String and advanced function concept
* 문자열
- 시퀀스 자료형으로 문자형 data를 메모리에 저장
- 영문자 한 글자는 1byte의 메모리 공간을 사용

각 타입 별로 크기가 다름
int - 4 byte
long - 무제한
float - 8 byte

- 문자열의 각 문자는 개별 주소(offset)을 가짐
- 이 주소를 사용하여 할당된 값을 가져올 수 있다. -> 인덱싱, list와 같다.

- 덧셈과 뺄셈, 곱하기 연산 가능 : 두 문자 연결, 문자열 반복
- in 명령으로 포함 여부 체크 가능

- 그 외에도, len(), upper, lower, capitalize, title, count, find, rfind, startswith, endswith,
  strip, rstrip, lstrip, split, isdigit, islower, isupper 등이 있다.
  


5) call by object reference
* 함수에서 파라미터를 전달하는 방식
(1) 값에 의한 호출 (call by value)
함수에 인자를 넘길 때 값만 넘긴다.
함수 내에 인자 값 변경 시, 호출자에게 영향을 주지 않는다.

(2) 참조에 의한 호출 (call by reference)
함수에 인자를 넘길 때 메모리 주소를 넘긴다.
함수 내에 인자 값 변경 시, 호출자의 값도 변경된다.

(3) 객체 참조에 의한 호출 (call by object reference)
파이썬은 객체의 주소가 함수로 전달되는 방식인데,
이 방식은 전달된 객체를 참조하여 변경 시 호출자에게 영향을 주지만
새로운 객체를 만들 경우 호출자에게 영향을 주지 않는다.
ex)
def spam(eggs) :
    eggs.append(1)
    eggs = [2, 3]
    
ham = [0]
spam(ham)
print(ham) -> [0, 1]



6) 변수의 범위 (Scoping Rule)
- 변수가 사용되는 범위 (함수 또는 메인 프로그램)
- 지역변수 (local variable) : 함수 내에서만 사용
- 전역변수 (global variable) : 프로그램 전체에서 사용

* 함수 내에서 전역변수 사용시 global 키워드 사용
def f() :
    global s
    s = 'I love London !'
    print(s)

s = 'I love Paris !'
f()
print(s)

-> 'I love London !'
-> 'I love London !' s가 함수 안에서 바뀌어 할당된다.



7) Recursive Function
- 자기 자신을 호출하는 함수
- 점화식과 같은 재귀적 수학 모형을 표현할 때 사용
- 재귀 종료 조건 존재, 종료 조건까지 함수 호출 반복

ex)
def factorial(n) :
    if n == 1 :
        return 1
    else :
        return n + factorial(n - 1)
        
print(factorial(int(input('Input Number for Factorial Calculation : '))))



8) Function type hints
- 파이썬의 가장 큰 특징인 dynamic typing에는 
처음 함수를 사용하는 사용자가 interface를 알기 어렵다는 단점이 있기 때문에 hint 사용
- 사용자에게 interface를 명확하게 알려줄 수 있고,
  함수의 문서화 시 parameter에 대한 정보도 알 수 있다.
- mypy 또는 IDE, linter 등을 통해 코드의 발생 가능한 오류를 사전에 확인할 수 있다.
- 시스템의 전체적인 안정성을 확보할 수 있다.

def do_function(var_name : var_type) -> return_type :
    pass

ex)
def type_hint_example(name : str) -> str :
    return f'hello, {name}'
    


9) Function Docstring
- 파이썬 함수에 대한 상세한 스펙(summary, args, return 등)을 사전에 작성하여 사용자의 이행도를 증진시킨다.
- 함수 안에, 세 개의 따옴표로 docstring 영역 표시(함수명 아래)



10) 함수 작성 가이드 라인
- 함수는 가능하면 짧게 작성할 것
- 함수의 이름에 함수의 역할과 의도가 명확히 드러나도록 만들 것
  verb_object 의 형식으로 만든다. ex) count_word()
  


"""
