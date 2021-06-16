"""
2021.06.15 수요일

[AI Tech Pre-course] 인공지능(AI) 기초 다지기
Chapter2. 파이썬 다지기

4. Python data handling

"""


"""
1. CSV : Comma Separate Value
- csv, 필드를 쉼표로 구분한 텍스트 파일
- 엑셀 양식의 데이터를 프로그램에 상관없이 쓰기 위한 데이터 형식
- 탭(TSV), 빈칸(SSV) 등으로 구분해서 만들기도 함
- 통칭하여 character-separated values(CSV) 로 부름
- 엑셀에서는 '다른 이름 저장' 기능으로 사용 가능


* 엑셀로 csv 파일 만들기
1) 파일 다운로드
2) 파일 열기
3) 파일 -> 다른 이름으로 저장 -> csv(쉼표로 분리) 선택 -> 파일명 입력
4) 엑셀 종료 후 notepad로 파일 열어보기


* 파이썬으로 csv 파일 읽기 / 쓰기
- text 파일 형태로 데이터 처리 예제
- 일반적 texfile을 처리하듯 파일을 읽어온 후, 한줄씩 처리


* csv 객체로 csv 처리
- text 파일 형태로 데이터를 처리하면 문장 내에 들어가있는 ',' 등에 대해
  전처리를 해줘야하는 문제점이 생긴다.
- 파이썬에서는 간단히 csv 파일을 처리하기 위해 csv 객체를 제공
- 한글로 되어있다면 별도의 처리 필요


"""



"""
2. 웹 (html)
- world wide web = web
- 우리가 늘 쓰는 인터넷 공간의 정식 명칭
- 팀 버너스리에 의해 1989년 처음 제안, 물리학자들 간의 정보교환 용
- 데이터 송수신을 위한 http 프로토콜 사용
- 데이터를 표시하기 위해 html 형식을 사용


* 웹은 어떻게 동작할까 ?
1) 요청 : 웹주소, form, header 등
2) 처리 : database 처리 등 요청 대응
3) 응답 : html, xml 등으로 결과 반환
4) 렌더링 : html, xml 표시


* HTML
- 웹 상의 정보를 구조적으로 표현하기 위한 언어
- 제목, 단락, 링크 등 요소 표시르 위해 tag 사용 (마크업 language)
- 모든 요소들은 <> 안에 둘러 쌓여 있음
- 모든 html은 트리 모양의 포함 관계를 가짐
- 일반적으로 웹 페이지의 html 소스파일은 
  컴퓨터가 다운로드 받은 후 웹 브라우저가 해석 / 표시


* html을 분석하는 방법
1) str
2) regular expression
3) beautiful / soup


* 정규식 (Regular Expression)
- 정규 표현식, regexp 또는 regex 등으로 불림
- 복잡한 문자열 패턴을 정의하는 문자 표현 공식
- 특정한 규칙을 가진 문자열의 집합을 추출
- 정규식을 위한 html parsing
    : 주민등록 번호, 전화번호, 도서 ISBN 등 
      형식이 있는 문자열을 원본 문자열로부터 추출한다.
      html 역시 tag를 사용하여 일정한 형식 존재 -> 정규식 추출 용이


* 정규식 기본 문법
1) 문자 클래스 [] : [] 사이의 문자들과 매치되는 것, -로 범위 표현 가능
     ex) [abc] -> 'a', 'before', 'cycle'

2) 원래의 의미와 다른 기호의 사용
. : 줄바꿈 문자인 \n을 제외한 모든 문자와 매치
* : 앞에 있는 글자가 반복해서 나올 수 있음
+ : 앞에 있는 글자를 최소 1회 이상 반복

3) {m.n} : 반복 횟수 지정
4) ? : 반복 1회
5) | : or, ^ : not


* 정규식 in 파이썬
- re 모듈
- 함수 : search = 한 개만 찾기, findall = 전체 찾기
- 추출된 패턴은 tuple로 반환


"""



"""
3. XML _ eXtensible Markup Language
- 데이터의 구조와 의미를 설명하는 TAG(markup)를 사용하여 표시하는 언어
- 태그와 태그 사이에 값이 표시되고, 구조적인 정보를 표현할 수 있음
- html과 문법 비슷, 대표적인 데이터 저장 방식
- 정보의 구조에 대한 정보인 스키마와 DTD 등으로 메타 정보 표현,
  용도에 따라 다양한 형태로 변경 가능
- XML은 컴퓨터(pc <-> 스마트폰) 간 정보를 주고받기 매우 유용

ex)
<?xml version='1.0'?>
<고양이>
    <이름>나비</이름>
    <품종>샴</품종>
    <나이>6</나이>
</고양이>

==> 트리 구조 !!


* XML parsing in Python
- xml도 html과 같이 구조적 markup 언어
- 정규표현식으로 parsing 가능 but, 더 쉬운 도구 있음
- 가장 많이 쓰이는 parser인 beautifulsoup으로 파싱

ex)
conda install lxml
conda install -c anaconda beautifulsoup4
from bs4 import BeautifulSoup               # 모듈 호출

with open('books.xml', 'r', encoding='uft8') as books_file :
    books_xml = books_file.read()           # 파일을 str로 읽어오기

soup = BeautifulSoup(books_xml, 'lxml')     # 객체 생성


for book_info in soup.find_all('author') :  # tag를 찾는 함수 find_all
    # author가 들어간 모든 element 추출, 출력
    print(book_info)
    print(book_info.get_text())
                

"""



"""
4. JSON _ JavaScript Object Notation
- 웹 언어인 JS의 데이터 객체 표현 방식
- 간결성으로 기계 / 인간 모두 이해하기 편함
- 데이터 용량이 적고, code로의 전환이 쉬움
- 이로 인해 xml의 대체재로 많이 활용


* Json in Python
- json 모듈을 사용하여 파싱, 저장 가능
- 데이터 저장 및 읽기는 dict type과 상호 호환 가능
- 웹에서 제공하는 api는 대부분 정보 교환 시 json 활용
- 페이스북, 트위터, 깃허브 등 거의 모든 사이트
- 각 사이트 마다 developer api의 활용법 찾아 사용
- json 파일 구조 확인 -> 읽어온 후 -> dict type처럼 처리
   -> dict type으로 저장 -> json모듈로 write


"""




