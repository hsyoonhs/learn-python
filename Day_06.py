# # time 모듈 사용하기
# import time

# # 변수 선언
# number = 0

# # 5초간 반복
# target_tick = time.time() + 5
# while time.time() < target_tick:
#     number += 1

# # 텍스트 출력
# print("5초 동안 {}번 반복했습니다.".format(number))

# ------------------------------ #

# aa = [0, 0, 0, 0]
# total = 0

# aa[0] = int(input("1번째 숫자: "))
# aa[1] = int(input("2번째 숫자: "))
# aa[2] = int(input("3번째 숫자: "))
# aa[3] = int(input("4번째 숫자: "))

# total = aa[0] + aa[1] + aa[2] + aa[3]

# print("합계: %d" % total)

# ------------------------------ #

# aa = []

# for i in range(0, 4):
#     aa.append(0)

# total = 0

# for i in range(0, 4):
#     aa[i] = int(input(str(i + 1) + "번째 숫자: "))

# for i in range(0, 4):
#     total += aa[i]

# print("합계: %d" % total)

# ------------------------------ #

# aa = [10, 20, 30, 40]

# # 음수값으로 접근
# print("aa = [10, 20, 30, 40]일 때")
# print("aa[-1]은 %d, aa[-2]는 %d \n" % (aa[-1], aa[-2]))

# # 콜론으로 범위 접근
# print(aa[0:3], aa[2:4], "\n")

# # 콜론으로 범위 접근 - 콜론 전후 생략
# print(aa[2:], aa[:2])

# ------------------------------ #

# 리스트끼리 연산
# aa = [10, 20, 30]
# bb = [40, 50, 60]

# print(aa + bb, aa * 3)

# ------------------------------ #

# 항목을 건너뛰며 접근
# aa = [10, 20, 30, 40, 50, 60, 70]

# print(aa[::2])
# print(aa[::-2])
# print(aa[::-1])

# print(aa[1::2])
# print(aa[1:7:2])

# ------------------------------ #

# 리스트 값의 변경
# aa = [10, 20, 30]
# aa[1] = 200
# print(aa)

# aa = [10, 20, 30]
# aa[1:2] = [200, 201]
# print(aa)

# ------------------------------ #

# aa = [10, 20, 30]
# aa[1] = [200, 201]
# print(aa)

# ------------------------------ #

# 삭제
# aa = [10, 20, 30]
# del(aa[1])
# print(aa)

# 범위를 지정하여 삭제
# aa = [10, 20, 30, 40, 50]
# aa[1:4] = [];
# print(aa)

# 리스트를 비우기 (빈 리스트 출력됨)
# aa = [10, 20, 30]
# aa = []
# print(aa)

# # 리스트를 None으로 만들기 (None 출력됨)
# aa = [10, 20, 30]
# aa = None
# print(aa)

# 리스트 자체를 제거 (출력될 수 없음)
# aa = [10, 20, 30, 40]
# print(aa)
# del(aa)
# print(aa)

# ------------------------------ #

# 다양한 리스트 함수
# myList = [30, 10, 20]
# print("현재 리스트: %s \n" % myList)

# myList.append(40)
# print("append(40) 후의 리스트: %s \n" % myList)

# print("pop()으로 추출한 값: %s" % myList.pop())
# print("pop() 후의 리스트: %s \n" % myList)

# myList.sort()
# print("sort() 후의 리스트: %s \n" % myList)

# myList.reverse()
# print("reverse() 후의 리스트: %s \n" % myList)

# print("20 값의 위치: %d \n" % myList.index(20))

# myList.insert(2, 222)
# print("insert(2, 222) 후의 리스트: %s \n" % myList)

# myList.remove(222)
# print("remove(222) 후의 리스트: %s \n" % myList)

# myList.extend([77, 88, 77])
# print("extend([77, 88, 77]) 후의 리스트: %s \n" % myList)

# print("77 값의 개수: %d" % myList.count(77))

# ------------------------------ #

# 2차원 리스트
# aa = [
#       [1, 2, 3, 4],
#       [5, 6, 7, 8],
#       [9, 10, 11, 12]
#      ]

# print(aa[1][2])

# ------------------------------ #

# list1, list2 = [], []
# value = 1

# for i in range(0, 3):
#     for k in range(0, 4):
#         list1.append(value)
#         value += 1
#     list2.append(list1)
#     list1 = []

# for i in range(0, 3):
#     for k in range(0, 4):
#         print("%3d" % list2[i][k], end="")
#     print("")

# ------------------------------ #

list1, list2 = [], []
value = 0

for i in range(0, 4):
    for k in range(0, 5):
        list1.append(value)
        value += 3
    list2.append(list1)
    list1 = []

for i in range(0, 4):
    for k in range(0, 5):
        print("%3d" % list2[i][k], end="")
    print("")