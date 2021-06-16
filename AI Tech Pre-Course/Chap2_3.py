"""
2021.06.15 수요일

[AI Tech Pre-course] 인공지능(AI) 기초 다지기
Chapter2. 파이썬 다지기

3. File / Exception / Log Handling

"""


"""
1. Exception
1) 예상 가능한 예외
 - 발생 여부를 사전에 인지할 수 있는 예외
 - 사용자의 잘못된 입력, 파일 호출 시 파일 없음
 - 개발자가 반드시 명시적으로 정의 해야함
 - if 문으로 해결 가능
 
2) 예상 불가능한 예외
 - 인터프리터 과정에서 발생하는 예외
 - 리스트의 범위를 넘어가는 값 호출, 정수를 0 으로 나눔
 - 수행 불가시 인터프리터가 자동 호출
 - Exception Handling으로 해결 가능
 
 
 
2. Exception Handling
- try ~ except 문법
try :
    예외 발생 가능 코드
except <Exception Type> :
    예외 발생시 대응하는 코드

위 코드에서 맨 하단에 else문이나 finally문도 추가할 수 있다.
else :
    예외가 발생하지 않을 때 동작하는 코드

finally :
    예외와 상관없이 항상 실행되는 코드
    print('종료되었습니다')


ex) 0으로 숫자를 나눌 때 예외처리 하기
for i in range(10) :
    try :
        print(10 / i)
    except ZeroDivisionError :       # for문 중간에서 예외 발생하여 except 구문 실행돼도
        print('Not divided by 0')    # 다시 그 다음 for문 실행한다.


* Built-in Exception, 기본적으로 제공하는 예외
- IndexError         : 리스트의 인덱스 범위를 넘어갈 때
- NameError          : 존재하지 않는 변수를 호출할 때
- ZeroDivisionError  : 0으로 숫자를 나눌 때
- ValueError         : 변환할 수 없는 문자 / 숫자를 변환할 때
- FileNotFoundError  : 존재하지 않는 파일을 호출할 때


"""



"""
3. File Handlig
* 파일 시스템
- os에서 파일을 저장하는 트리구조 저장 체계

- 기본적인 파일 종류로는 text와 binary파일이 있다.
  binary 파일 
   : 컴퓨터만 이해할 수 있는 형태인 이진법 형식으로 저장된 파일
     일반적으로 메모장으로 열면 내용이 깨져보임 (메모장 해설 불가)
     엑셀파일, 워드 파일 등등
  text 파일
   : 인간도 이해할 수 있는 형태인 문자열 형식으로 저장된 파일
     메모장으로 열면 내용 확인 가능
     메모장에 저장된 파일, html 파일, 파이써 코드 파일 등등
     
- 컴퓨터는 text 파일을 처리하기 위해 binary 파일로 변환하므로
  모든 text 파일은 실제로 binary 파일이다.
  Ascii / unicode 문자열 집합으로 저장되어 사람이 읽을 수 있다.


* file form wiki
- 컴퓨터 등의 기기에서 의미있는 정보를 담는 논리적인 단위
모든 프로그램은 파일로 구성되어 있고, 파일을 사용한다.


* open 키워드
- 파이썬이 파일 처리를 위해 사용하는 키워드
f = open('<파일 이름>', '접근 모드')
f.close()

- 파일 열기 모드
  r : 읽기 모드, 파일을 읽기만 할 때 사용
  w : 쓰기 모드, 파일에 내용을 쓸 때 사용
  a : 추가 모드, 파일의 마지막에 새로운 내용을 추가할 때 사용


1) 파이썬의 File Read
ex) 대상 파일이 같은폴더에 있을 경우
f = open('i_have_a_dream.txt', 'r')
contents = f.read()                 # read() = txt 파일의 내용을 문자열로 반환
print(contents)
f.close()

ex) with 구문과 함께 사용하기
with open('i_have_a_dream.txt', 'r') as my_file :
    contents = my_file.read()
    print(type(contents), contents)

ex) 한 줄씩 읽어 list type으로 반환하기
with open('i_have_a_dream.txt', 'r') as my_file :
    contents_list = my_file.readlines()     # 파일 전체를 list로 반환
    print(type(contents_list))              # type 확인
    print(contents_list)                    # 리스트 값 출력

ex) 실행될 때마다 한 줄씩 메모리에 올려 읽어오기
왜 ? 용량이 너무 크거나 ...
with open('i_have_a_dream.txt', 'r') as my_file :
    i = 0
    while True :
        line = my_file.readline()
        if not line :
            break
        print(str(i) + '===' + line.replace('\n',''))   # 한줄씩 값 출력
        i = i + 1


2) 파이썬의 File Write
- encoding : utf8, utf16은 동아시아에서 많이 사용
             cp949는 윈도우에서 많이 사용
ex) 
f = open('count_log.txt', 'w', encoding='utf8')
for i in range(1, 11) :
    data = '%d번 째 줄 입니다.\n' % i
    f.write(data)
f.close()


3) 파이썬의 File Append
ex) 
f = open('count_log.txt', 'a', encoding='utf8')
for i in range(11, 21) :
    data = '%d번 째 줄 입니다.\n' % i
    f.write(data)
f.close()


4. 파이썬의 directory 다루기
- os 모듈을 사용하여 directory 다루기
import os
os.mkdir('log')

- 디렉토리가 있는지 확인하기
1)
if not os.path.isdir('log') :
    os.mkdir('log')
2)
os.path.exists('log')
 >>> True

- 파일을 다른 디렉토리로 옮기기
1) shutil 사용하기
import shutil

source = 'file.ipynb'
dest = os.path.join('abc', 'file.ipynb')
shutil.copy(sourse, dest)      # 파일 복사 함수

2) pathlib 모듈로 path 객체로서 다루기
import pathlib
cwd = pathlib.Path.cwd()       # 현재의 경로를 객체로 만듦
cwd    
cwd.parent                     # 현재 경로보다 상위의 폴더


"""



"""
5. Pickle
- 파이썬의 객체를 영속화(persistence)하는 built-in 객체
- 데이터, object 등 실행 중 정보를 저장 -> 불러와서 사용
- 저장해야하는 정보, 계산 결과(모델) 등 활용이 많음

- 피클은 파이썬에 특화된 바이너리 파일 !!

import pickle
f = open('list.pickle', 'wb')      # wb = write binary
test = [1, 2, 3, 4, 5]
pickle.dump(test, f)
f.close()

del test            # 메모리에서 test 지우기. but, 피클 만들었으니 불러올수 있다.

f = open('list.pickle', 'rb')       # rb = read binary
test_pickle = pickle.load(f)
print(test_pickle)                  # [1, 2, 3, 4, 5] 출력됨
f.close()


* 클래스도 피클로 만들어서 사용할 수 있다.


"""



"""
6. Logging Handlig
* Logging
- 프로그램이 실행되는 동안 일어나는 정보를 기록하는 것
- 유저의 접근, 프로그램의 Exception, 특정 함수의 사용
- 콘솔 화면에 출력, 파일에 남기기, db에 남기기 등
- 기록된 로그를 분석하여 의미있는 결과를 도출할 수 있다.
- 실행 시점에서 남겨야 하는 기록, 개발 시점에서 남겨야 하는 시록


* print vs. logging
- 기록을 print로 남기는 것도 가능하지만 콘솔창에만 남기는 기록 분석시 사용 불가
- 때로는 레벨별(개발, 운영)로 기록 남길 필요도 있다.
- 모듈별로 별도의 logging을 할 필요도 있다.
- 이러한 기능을 체계적으로 지원하는 모듈 필요


* logging level
import logging
logging.debug()       : 개발시 처리 기록을 남겨야하는 로그 정보를 기록
 ex) 다음 함수로 a를 호출함, 변수 b를 c로 변경함
 
logging.info()        : 처리가 진행되는 동안의 정보를 알림
 ex) 서버가 시작됨, 종료됨, 사용자 a가 프로그램에 접속함
 
logging.warning()     : 사용자가 잘못 입력한 정보나, 
                        처리할 수 있지만 의도치 않은 정보가 들어왔을 때 알림
 ex) str 입력을 기대했으나 int가 입력됨
        -> str casting으로 처리함
     함수의 argument로 2차원 리스트를 기대했으나 1차원 리스트가 들어옴
        -> 2차원으로 변환 후 처리함
        
logging.error()       : 잘못된 처리로 에러가 났으나 프로그램 동작은 가능할 때 알림
 ex) 파일에 기록해야하지만 그 파일이 없음
        -> exception 처리 후 사용자에게 알림
     외부 서비스와 연결 불가
     
logging.critical()    : 잘못된 처리로 데이터가 손실되거나 프로그램이 동작할 수 없음을 알림
 ex) 잘못된 접근으로 해당 파일이 삭제됨
     사용자에 의한 프로그램 강제 종료


* configparser
- 프로그램의 실행 설정을 file에 저장
- Section, Key, Value 값의 형태로 설정된 설정 파일을 사용
- 설정파일을 dict type으로 호출 후 사용


* argparser
- 콘솔 창에서 프로그램 실행시 setting 정보를 저장
- 거의 모든 콘솔 기반 python 프로그램에서 기본으로 제공
- 특수 모듈도 많이 존재하지만 (TF), 일반적으로 argparser를 사용
- command-line option 이라고 부름


* logging formmater
- 로그의 결과값의 format을 지정해줄 수 있음
ex)
formmater = logging.Formatter('%(asctime)s %(levelname)s 
                               %(process)d %(message)s')
                               

"""




