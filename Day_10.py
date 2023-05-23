# 매개변수에 기본값을 설정해놓고 전달하는 방법

# def para_func(v1, v2, v3 = 0, v4 = 0):
#     result = 0
#     result = v1 + v2 + v3 + v4
#     return result

# hap = 0

# hap = para_func(10, 20)
# print("함수의 매개변수를 2개 넣고 호출한 결과 ==> %d" % hap)
# hap = para_func(10, 20, 30)
# print("함수의 매개변수를 3개 넣고 호출한 결과 ==> %d" % hap)
# hap = para_func(10, 20, 30, 40)
# print("함수의 매개변수를 4개 넣고 호출한 결과 ==> %d" % hap)

# ------------------------------ #

# 튜플 형식으로 매개변수 전달

def para_func(*para):
    result = 0
    for num in para:
        result = result + num

    return result

hap = 0

hap = para_func(10, 20)
# print("함수의 매개변수를 2개 넣고 호출한 결과 ==> %d" % hap)
hap = para_func(10, 20, 30)
# print("함수의 매개변수를 3개 넣고 호출한 결과 ==> %d" % hap)
hap = para_func(10, 20, 30, 40)
# print("함수의 매개변수를 4개 넣고 호출한 결과 ==> %d" % hap)

# 딕셔너리 형식으로 매개변수 전달

# def dic_func(**para):
#     for k in para.keys():
#         print("%s --> %d명입니다." % (k, para[k]))

# dic_func(트와이스 = 9, 소녀시대 = 7, 걸스데이 = 4, 블랙핑크 = 4)

# ------------------------------ #

# import random

# def getNumber():
#     return random.randrange(1, 46)

# lotto = []
# num = 0

# print("** 로또 추첨을 시작합니다 **\n")

# while True:
#     num = getNumber()
    
#     if lotto.count(num) == 0:
#         lotto.append(num)
    
#     if len(lotto) >= 6:
#         break

# print("추첨된 로또 번호 => ", end="")
# lotto.sort()
# for i in range(0, 6):
#     print("%d " % lotto[i], end="")

# ------------------------------ #

## 파일 입출력 (기말고사 범위 아님)

# inFp = None # 입력 파일
# inStr = "" # 읽어온 문자열

# inFp = open("C:/Temp/data1.txt", "r", encoding="UTF-8")

# inStr = inFp.readline() # readline() 함수가 inFp로 열린 파일에서 한 행 읽어 inStr에 저장
# print(inStr, end="") # 화면에 출력

# inStr = inFp.readline()
# print(inStr, end="")

# inStr = inFp.readline()
# print(inStr, end="")

# inFp.close() # 파일 닫기

# ------------------------------ #

# 반복문을 통한 개선

inFp = None # 입력 파일
inStr = "" # 읽어온 문자열

inFp = open("C:/Temp/data1.txt", "r", encoding="UTF-8") # 읽기 모드 r

while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print(inStr, end="")

inFp.close() # 파일 닫기

# ------------------------------ #

outFp = None
outStr = ""

outFp = open("C:/Temp/data2.txt", "w") # 쓰기 모드 w

while True:
    outStr = input("내용 입력: ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close() # 파일 닫기
print("--- 정상적으로 파일에 씀 ---")

# ------------------------------ #

## 객체 지향 프로그래밍 (Object-oriented programming, OOP)
# (절차적 프로그래밍(Procedural programming)과 반대되는 개념)

# ------------------------------ #

# class의 개념 (메인 코드와 분리된 곳에 있는 것)

class Car:
    # 자동차의 속성 (변수와 같으나 class에선 "필드")
    color = ""
    speed = 0

    # 자동차의 기능 (함수와 같으나 class에선 "메서드")
    def upSpeed (self, value):
        self.speed += value

    def downSpeed (self, value):
        self.speed -= value

# self.speed는 class 초반의 speed, 즉 자신의 class에 있는 speed 변수 의미

# ------------------------------ #

# 인스턴스의 개념
    # 메인 코드에서 class를 사용하기 위해 생성하는 object
    # 필요한 만큼 생성할 수 있음

myCar1 = Car()
myCar2 = Car()
myCar3 = Car()

# 인스턴스 필드 값 대입
    # 인스턴스명.필드명

myCar1.color = "빨강" # 서로 다른 인스턴스의 필드(변수)는 온전히 개별적으로 기능
myCar1.speed = 0
myCar2.color = "파랑"
myCar2.speed = 0
myCar3.color = "노랑"
myCar3.speed = 0

# 인스턴스 메서드 호출
    # 인스턴스명.메서드()

myCar1.upSpeed(30)
myCar2.upSpeed(60)
myCar3.upSpeed(0)

# ------------------------------ #

# 예제

# class 선언

class Boat:
    color = ""
    speed = 0

    def speedUp(self, value):
        self.speed += value

    def speedDown(self, value):
        self.speed -= value

# 메인 코드

myBoat1 = Boat()
myBoat1.color = "빨강"
myBoat1.speed = 0

myBoat2 = Boat()
myBoat2.color = "파랑"
myBoat2.speed = 0

myBoat3 = Boat()
myBoat3.color = "노랑"
myBoat3.speed = 0

myBoat1.speedUp(30)
print("보트1의 색상은 %s이며, 현재 속도는 %d km입니다." % (myBoat1.color, myBoat1.speed))

myBoat2.speedUp(60)
print("보트2의 색상은 %s이며, 현재 속도는 %d km입니다." % (myBoat2.color, myBoat2.speed))

myBoat3.speedUp(0)
print("보트3의 색상은 %s이며, 현재 속도는 %d km입니다." % (myBoat3.color, myBoat3.speed))