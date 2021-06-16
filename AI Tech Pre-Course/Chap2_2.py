"""
2021.06.05 토요일

[AI Tech Pre-course] 인공지능(AI) 기초 다지기
Chapter2. 파이썬 다지기

2. Module and Project

"""

"""
1. 모듈과 패키지
* 모듈
- 어떤 대상의 부분 혹은 조각 ex) 레고 블록, 벽돌, 자동차 부품 등
- 모듈들을 모아서 하나의 큰 프로그램을 개발
- 파이썬의 모듈 == py 파일
- 같은 폴더에 모듈에 해당하는 .py파일과 사용하는 .py를 저장한 후 import문으로 호출


ex)
import fah_converter                  # fah_converter.py 불러오기
fah_converter.convert_c_to_f(42.6)    # fah_converter의 convert_c_to_f 함수에 42.6 전달

__pycache__   :   .py파일을 기계어로 컴파일한 파일이 들어있다.


1) alias 설정하기 _ 모듈명을 별칭으로 써서
import fah_converter as fah
print(fah.conver_c_to_f(42.6))

2) 모듈에서 특정 함수 또는 클래스만 호출하기
from fah_converter import convert_c_to_f
print(convert_c_to_f(42.6))

3) 모듈에서 모든 함수 또는 클래스 호출하기
from fah_converter import *
print(convert_c_to_f(42.6))

* built-in modules
- 파이썬이 기본 제공하는 라이브러리
- 문자처리, 웹, 수학 등 다양한 모듈 제공
- 별다른 조치없이 ipmort문으로 활용 가능
ex)
import random
random.randint(0, 100)     # 0에서 100까지의 정수 난수 생성

ex)
import time
print(time.localtime())    # 현재 시간 출력

ex)
import urllib.request
response = urllib.request.urlopen('http://naver.com')
print(response.read())


* 수많은 모듈을 어떻게 검색할까 ? 
- 구글에 검색
- 모듈 import 후 구글 검색 또는 help 쓰기
- 공식 문서 읽어보기

"""



"""
* 패키지
- 모듈을 모아놓은 단위, 하나의 프로그램
- 하나의 대형 프로젝트를 만드는 코드의 묶음, 폴더로 연결됨
- __init__, __main__ 등 키워드 파일명이 사용됨
- 다양한 오픈 소스들이 모두 패키지로 관리됨

* 패키지 만드는 순서               # game package
1) 기능 별로 폴더 만들기           # stage, image, sound
2) 각 폴더별로 필요한 모듈 생성     # 각 폴더에는 __init__.py가 있어야 함     
def echo_play() :              # image : __init__.py, character.py, object.py
    return 'Hello Echo'        # sound : __init__.py, echo.py, bgm.py
                               # stage : __init__.py, main.py, sub.py

3) 모듈 불러오기
python                         # python 실행
from sound import echo         # sound 폴더의 echo 모듈 불러오기
echo.echo_play()               # echo 모듈의 echo_play() 함수 실행
>>> 'Hello Echo'               # echo_play() 실행되어 'Hello Echo' 출력

4) 폴더별로 __init__.py 구성하기
- 현재 폴더가 패키지임을 알리는 초기화 스크립트
- 없을 경우 패키지로 간주하지 않음 (3.3+ 부터는 x)
- 하위 폴더와 py파일(모듈)을 모두 포함함
- ipmort와 __all__keyword 사용

ex) 제일 상단의 __init__.py 만들기
__all__ = ['image', 'sound', 'stage']

from . import image
from . import sound
from . import stage

ex) sound의 __init__.py 만들기           # image와 stage도 해줘야 함
__all__ = ['bgm', 'ehco']

from . import bgm
from . import echo


5) __main__.py 만들기
from sound import echo

if __name__ == '__main__' :
    print('Hello Game')
    print(echo.echo_play())
    
    
* 패키지 내에서 다른 폴더의 모듈을 부를 때 상대 참조로 호출하는 방법
1) 절대 참조
from game.graphic.render import render_test()

2) . 현재 디렉토리 기준 (상대 참조)
from .render import render_test()

3) .. 부모 디렉토리 기준 (상대 참조)
from ..sound.echo improt echo_test()


"""



"""
* 가상환경 설치하기
- 프로젝트 진행 시 필요한 패키지만 설치하는 환경
- 기본 인터프리터 + 프로젝트 종류별 패키지 설치
 ex) 웹 프로젝트, 데이터 분석 프로젝트 _ 각각의 패키지를 관리할 수 있는 기능
 
- 다양한 패키지 관리 도구를 사용함
 ex) virtualenv + pip : 가장 대표적인 가상환경 관리 도구
                        레퍼런스 + 패키지 개수
     conda : 상용 가상환경 도구, miniconda 기본 도구
             설치의 용이성, windows에서 장점
             
ex) 가상환경 예제
conda create -n my_project python=3.9
conda activate my_project              # 가상환경 활성화
  base)  ->  my_project) 로 바뀜
conda install matplotlib               # matplotlib 패키지 설치
conda install tqdm                     # loop의 진행상황, 잔여시간 표시
conda install jupyter

* matplotlib
- 대표적인 파이썬 그래프 관리 패키지
- 엑셀과 같은 그래프들을 화면에 표시함
- 다양한 데이터 분석 도구들과 함께 사용됨
  
"""














