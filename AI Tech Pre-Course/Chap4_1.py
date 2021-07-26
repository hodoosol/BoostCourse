"""
2021.06.16 목요일

[AI Tech Pre-course] 인공지능(AI) 기초 다지기
Chapter4. 기초 튼튼, 수학 튼튼

1. Pandas I

"""


"""
1. Pandas
- 구조화된 데이터의 처리를 지원하는 python 라이브러리
- 고성능 array 계산 라이브러리인 numpy와 통합하여 강력한 스프레드시트 처리 기능 제공
- 인덱싱, 연산용 함수, 전처리 함수 등을 제공

import pandas as pd

data_url = 'https:// ... 어쩌구'
df_data = pd.read_csv(data_url, sep='\s+', header=None)
 -> csv 타입 데이터 로드, 데이터를 나누는 기준은 빈칸으로 나눔

df_data.columns  -> 데이터의 컬럼 추출 
df_data.values   -> 데이터의 값 추출


* 판다스의 구성 
Series : DataFrame 중 하나의 Column에 해당하는 데이터외 모음 object
DataFrame : Data Table 전체를 포함하는 object, 기본적으로 2차원


* 판다스 다루기
# 특정한 컬럼만 선택하여 가져오기
DataFrame(raw_data, columns = ['age', 'city'])

# 새로운 컬럼 추가
DataFrame(raw_data, columns = ['age', 'city', 'debt'])

# 컬럼을 선택하여 시리즈로 추출 _ 두가지 방법
1)
df.age
2)
df['age']

# loc : index location 인덱스 이름을 넣어서 데이터 추출
# iloc : index position 인덱스 번호를 넣어서 데이터 추출

# 컬럼에 새로운 데이터 할당
df.debt = df.age > 40
 -> debt를 age 컬럼의 데이터가 40이 넘는다면 True, 넘지않으면 False로 채운다.

# transpose
df.T

# csv 변환
df.to_csv()

# 컬럼 삭제
del df['debt']

# selection with column names
- 한개의 컬럼 선택시
df['account'].head()
- 한개 이상의 컬럼 선택시
df[['account', 'street']].head()

# selection with Series
- 한개의 인덱스 선택시
account_series[:3]
- 한개 이상의 인덱스 선택시
account_series[[0, 1, 2]]

# 인덱스 변경
df.index = df['account']
 -> account의 값으로 인덱스를 변경함
del df['account']

# 인덱스 재설정
df.index = list(range(0, 15))

# 컬럼 단위로 데이터 삭제
df.drop(1)
 -> inplace=True 하지 않으면 원본데이터 그대로 유지

# 시리즈 연산
s1 = Series(range(1, 6), index = list('abcde'))
s1 = Series(range(5, 11), index = list('bcedef'))

s1.add(s2)    or   s1 + s2
a  NaN
b   7
c   9
d  13
e  11
e  13
f  NaN
인덱스를 기준으로 연산 수행, 겹치는 인덱스가 없으면 nan 값 반환


"""





