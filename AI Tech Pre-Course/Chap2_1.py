"""
2021.06.05 토요일

[AI Tech Pre-course] 인공지능(AI) 기초 다지기

Chapter2. 파이썬 다지기
1. Python object oriented programming

"""


"""
1) 객체지향 언어
* 수강신청 프로그램을 작성하려면 어떻게 해야할까 ?
 1. 수강신청이 이루어지는 순서대로 작성
 2. 수강신청 관련 주체들(교수, 학생, 관리자)의 행동(수강신청, 과목 입력)과
    데이터(수강과목, 강의과목) 들을 중심으로 프로그램 작성 후 연결

* Object-Oriented Programming = OOP
  객체 : 실생활에서 일종의 물건, 속성과 행동을 가짐
  OOP는 이러한 객체 개념을 프로그램으로 표현한 것
  속성 = 변수, 행동 = 함수로 표현됨
  OOP는 설계도에 해당하는 클래스와 실제 구현체인 인스턴스로 나뉘어짐
   붕어빵 틀 = class, 붕어빵 = instance
   
2) Objects in Python
- 축구 선수 정보를 class로 구현하기
class SoccerPlayer(object) :   # class 예약어 + class 이름 (상속받는 객체명)
     # 속성 추가 - __init__ = 객체 초기화 예약 함수 (속성 정보)
    def __init__(self, name : str, position : str, back_number : int) :  
        self.name = name
        self.position = position
        self.back_number = back_number
        
    def __str__(self) :
        return 'Hello, my name is %s. My back number is %d' % \
                (self.name, self.back_number)   
        
    def __add__(self, other) :
        return self.name + other.name
     
    def change_back_number(self, new_number) :
        print('선수의 등번호를 변경합니다 : From %d to %d' % (self.back_number, new_number))
        self.back_number = new_number   
   


3) Inheritance
class Person(object) :
    def __init__(self, name, age) :
        self.name = name
        self.age = age
        
    def __str__(self) :
        return '저의 이름은 {0} 입니다. 나이는 {1} 입니다.'.format(
            self.name, self.age
        )
# person 클래스 상속받기
class Korean(Person) :
    pass

# 상속을 받으면 부모클래스의 속성을 사용할 수 있다.
first_korean = Korean('dasol', 26)
print(first_korean)
 -> 저의 이름은 dasol 입니다. 나이는 26 입니다.
 
* super() => 부모 클래스의 속성들을 불러올 수 있다.



4) Polymorphism 다형성
- 같은 이름 메소드의 내부 로직을 다르게 작성
- dynamic typing 특성으로 인해 파이썬에서는 같은 부모 클래스의 상속에서 주로 발생

class Animal :
    def __init__(self, name) :
        self.name = name
    
    def talk(self) :
        raise NotImplementedError('Subclass must implement abstract method')
            class Cat(Animal) :
                def talk(self) :
                    return 'Meow!'
            
            class Dog(Animal) :
                def talk(self) :
                    return 'Woof! Woof!'
                    
animals = [Cat('Missy'), Cat('Mr. Mistoffelees'), Dog('Lassie')]

for animal in animals :
    print(animal.name + ': ' + anmial.talk())
 
 
 
5) Visibility 가시성
- 객체의 정보를 볼 수 있는 레벨을 조절
- 누구나 객체 안의 모든 변수를 볼 필요 x
   1. 객체를 사용하는 사용자가 임의로 정보 수정
   2. 필요 없는 정보에는 접근할 필요 없음
   3. 만약 제품으로 판매한다면 ? 소스 보호 필요
 
* 캡슐화 or 정보은닉 (Information Hiding)
- 클래스를 설계할 때, 클래스 간 간섭/정보공유의 최소화
- 심판 클래스가 축구선수 클래스의 가족 정보를 알아야 하나 ? x
- 캡슐을 던지듯, 인터페이스만 알아서 써야함

self.__items = []   ->   Private 변수로 선언하여 다른 객체가 접근할 수 없다.


   
6) 일급 함수 First-class objects
- 변수나 데이터 구조에 할당이 가능한 객체
- 파라미터로 전달 가능, 리턴 값으로 사용 가능
- 파이썬의 모든 함수는 일급함수이다.
   
ex 1)
def square(x) :
    return x * x

def cube(x) :
    return x * x * x
 
def formula(method, argument_list) :
    return [method(value) + for value in argument_list]
    
    
ex 2) 함수 내에 함수
def print_msg(msg) :
    def printer() :
        print(msg)
    return printer
    
        
 
"""


