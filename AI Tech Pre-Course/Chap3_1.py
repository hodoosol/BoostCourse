"""
2021.06.10 목요일

[AI Tech Pre-course] 인공지능(AI) 기초 다지기

Chapter3. 기초 수학 첫걸음
1. Numpy / 벡터 & 행렬

"""

# 1. Numerical Python - Numpy

## 기본적인 array 만들기
import numpy as np
array1 = np.array([1, 4, 5, 8], float)

# array 타입
print(type(array1[3]))

# array 모양
print(array1.shape)

# array 차원
print(array1.ndim)

# array 전체의 데이터 개수
print(array1.size)

# array의 메모리 크기
print(array1.nbytes)



## shape handling

# array shape의 크기 변경
array2 = np.array([[1, 2, 3, 4], [1, 2, 5, 8]], int)
print(array2.shape)

array2 = array2.reshape(2, 2, 2) # 2 * 4 행렬을 2 * 2 행렬 2장으로 변경
print(array2)

# flatten _ 다차원 array를 1차원으로 변환
array3 = np.array([[[1, 2, 3, 4], [1, 2, 5, 8]], [[1, 2, 3, 4], [1, 2, 6, 7]]], int)
array3 = array3.flatten()
print(array3)



## Indexing & Slicing

# Indexing _ 두 가지 방법
array4 = np.array([[1, 2, 3], [4, 5, 6]], int)
# 1
print(array4[0, 0])
# 2
print(array4[0][0])

# Slicing
array5 = np.array([[1, 2, 4, 7], [1, 5, 5, 7], [1, 7, 4, 32]], int)
# 2행, 모든 열 추출
print(array5[:2, :])
# 모든 행, 1열부터 2열까지
print(array5[:, 1:3])
# 1행에서 1열까지
print(array5[1, :2])



## Creation function

# arange _ array의 범위를 지정하여 값의 list를 생성하는 명령어
array6 = np.arange(30).reshape(5, 6)
print(array6)

# ones, zeros
array7 = np.zeros(shape=(10,), dtype=np.int8)
print(array7)

array8 = np.ones(shape=(10,), dtype=np.int8)
print(array8)

# empty _ shape만 주어지고 비어있는 ndarray 생성, momory initialization 되지 않음
array9 = np.empty(shape=(10,), dtype=np.int8)
print(array9)

array10 = np.empty((3, 5))
print(array10)

# ones_like(기존 array) - 기존 array와 똑같은 shape의 1 행렬을 만들어줌
# identity - 단위행렬 생성
# eye - 대각선이 1인 행렬 생성



## Concatenate

# vstack _ 행으로 합침
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
array11 = np.vstack((a, b))
print(array11)

# hstack _ 열로 합침
a = np.array([[1], [2], [3]])
b = np.array([[4], [5], [6]])
array12 = np.hstack((a, b))
print(array12)

# np.cocatenate((a, b), axis=0) == vstack
# np.cocatenate((a, b), axis=1) == hstack



# Operation b / t arrays _ array 끼리의 연산

# 곱하기의 경우
## 1. array간 shape이 같을 때 == element-wise *
## 2. matrix의 기본 연산, 내적 == dot()

# broadcasting _ shape이 다른 배열 간 연산
array13 = np.array([[1, 2, 3], [4, 5, 6]], float)
scalar = 3
array13 = array13 + scalar
print(array13)



# Comparison
array14 = np.arange(10)
print(array14 > 5)

# np.where _ 조건을 만족하는 인덱스 값 반환
print(np.where(array14 > 0, 3, 2)) # array14에서 0보다 큰 원소는 3을 반환, 작으면 2를 반환
print(np.where(array14 > 7)) # 7보다 큰 원소의 인덱스값 반환 -> 8, 9

# argmax & argmin
array15 = np.array([1, 4, 6, 87, 0 , 65])
print(np.argmax(array15), np.argmin(array15))



# Fancy index
a = np.array([2, 4, 6, 8], float)
b = np.array([0, 0, 1, 3, 2, 1], int) # 반드시 int로 선언
print(a[b]) # b가 인덱스로 동작하여 해당하는 값을 모두 추출




