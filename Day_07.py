## 튜플

tuple1 = (10, 20, 30)
print(tuple1)

tuple2 = 10, 20, 30
print(tuple2)

# ------------------------------ #

# 튜플은 읽기 전용이므로 값을 수정할 수 없음

# tuple1.append(40) # 'tuple' 객체엔 'append' 속성 없음
# tuple1[0] = 40 # 'tuple' 객체는 item 배정을 지원하지 않음
# del(tuple1[0]) # 'tuple' 객체는 item 삭제를 지원하지 않음

# del() 함수를 사용하여 아예 삭제할 수 있음

del(tuple1)
del(tuple2)

# ------------------------------ #

# 튜플 접근

tuple1 = (10, 20, 30, 40)
print(tuple1[0])
print(tuple1[0] + tuple1[1] + tuple1[2])

print(tuple1[1:3])
print(tuple1[1:])
print(tuple1[:3])

# ------------------------------ #

# 튜플 연산

tuple2 = ('A', 'B')
print(tuple1 + tuple2)
print(tuple2 * 3)

# ------------------------------ #

# 튜플 값 수정을 위한 <튜플 - 리스트 - 튜플> 변환

myTuple = (10, 20, 30)
myList = list(myTuple)
myList.append(40)
myTuple = tuple(myList)
print(myTuple)

# ------------------------------ #

# 튜플을 사용하는 이유:
    # 값 보호
    # 리스트 대비 적은 메모리, 빠른 속도

# 튜플 특징:
    # 서로 다른 데이터형 함께 수용 가능
    # 튜플 속 튜플 입력 (중첩) 가능
    # 리스트에서 가능한 연산 가능
    # 인덱싱할 때 대괄호 사용 (리스트와 동일)
    # 값 조작은 불가하나 접근 방식은 리스트와 유사

# ------------------------------ #

## 딕셔너리

Dict = {'apple': '사과', 'banana': '바나나'}
print(Dict['apple'])

# ------------------------------ #

student1 = {'학번': 1000, '이름': '홍길동', '학과': '컴퓨터학과'}
print(student1)

# 추가

student1['연락처'] = '010-1111-2222'
print(student1)

# 수정

student1['학과'] = '파이썬학과'
print(student1)

# 삭제

del(student1['학과'])
print(student1)

# 키로 값에 접근

print(student1['학번'])
print(student1['이름'])
print(student1['연락처'])

# get()으로 값에 접근

print(student1.get('이름'))

# ------------------------------ #

# key()로 모든 키 반환

print(student1.keys())

# 모든 키를 리스트로 변환

print(list(student1.keys()))

# values()로 모든 값 반환

print(student1.values())

# ------------------------------ #

# items()로 튜플 형태로 활용

print(student1.items())

# in으로 해당 키가 딕셔너리에 존재하는지 확인

print('이름' in student1) # True
print('주소' in student1) # False

# ------------------------------ #

# for 문으로 모든 딕셔너리 값 출력

singer = {}

singer['이름'] = '트와이스'
singer['구성원 수'] = 9
singer['데뷔'] = '서바이벌 식스틴'
singer['대표곡'] = 'SIGNAL'

for k in singer.keys():
    print('%s → %s' % (k, singer[k]))

# ------------------------------ #

# 딕셔너리 정렬 (가능하다는 것만 참고)

import operator

trainDict, trainList = {}, []

trainDict = {'Thomas': '토마스', 'Edward': '에드워드', 'Henry': '헨리', 'Gordon': '고든', 'James': '제임스'}
trainList = sorted(trainDict.items(), key = operator.itemgetter(0))

print(trainList)

# ------------------------------ #

# 예제

foods = {
    "떡볶이": "오뎅",
    "짜장면": "단무지",
    "라면": "김치",
    "피자": "피클",
    "맥주": "땅콩",
    "치킨": "치킨무",
    "삼겹살": "상추"
    }

# while True:
#     myFood = input(str(list(foods.keys())) + " 중 좋아하는 음식은? ")
#     if myFood in foods:
#         print("%s의 궁합 음식은 %s입니다." % (myFood, foods[myFood]))
#     elif myFood == "끝":
#         break
#     else:
#         print("그런 음식은 없습니다. 보기를 확인해 보세요.")

# ------------------------------ #

## 세트, 키만 모아놓은 딕셔너리의 특수 형태:
    # 딕셔너리 키는 중복하여 넣을 수 없으므로 하나씩만 기록됨

mySet = {1, 2, 3, 3, 3, 4}
print(mySet)

salesList = ['바나나', '바나나', '사과', '바나나', '바나나']
print(set(salesList))

# ------------------------------ #

# 세트 간의 교집합, 합집합, 차집합, 대칭 차집합

mySet1 = {1, 2, 3, 4, 5}
mySet2 = {4, 5, 6, 7}

print(mySet1 & mySet2)
print(mySet1 | mySet2)
print(mySet1 - mySet2)
print(mySet1 ^ mySet2)

print(mySet1.intersection(mySet2))
print(mySet1.union(mySet2))
print(mySet1.difference(mySet2))
print(mySet1.symmetric_difference(mySet2))

# ------------------------------ #

## 리스트, 튜플, 딕셔너리 심화

# zip()으로 동시에 여러 리스트 접근

mainDish = ['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살']
sideDish = ['오뎅', '단무지', '김치']

for mainDish, sideDish in zip(mainDish, sideDish):
    print(mainDish, ' → ', sideDish)

# ------------------------------ #

# zip()으로 두 리스트를 튜플이나 딕셔너리로 짝지음

mainDish = ['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살']
sideDish = ['오뎅', '단무지', '김치']

tupList = list(zip(mainDish, sideDish))
dic = dict(zip(mainDish, sideDish))

print(tupList)
print(dic)

# ------------------------------ #

# 리스트의 얕은 복사와 깊은 복사
    # 추가 정리 필요

# ------------------------------ #

# 리스트로 스택 구현
    # 추가 정리 필요