# class 선언
class Car:
    # 필드 (인스턴스 변수)
    color = ""
    speed = 0

    # 필드 (class 변수, 모든 인스턴스가 class 변수공간 공유)
    count = 0

    def __init__(self):
        self.speed = 0
        Car.count += 1

    def upSpeed (self, value):
        self.speed += value
        print("현재 속도(슈퍼 class): %d km" % self.speed)

    def downSpeed (self, value):
        self.speed -= value

myCar1, myCar2, myCar3 = None, None, None

# class 변수에 접근할 때는 'class명.class변수명' 또는 '인스턴스명.class변수명'으로 접근할 수 있다.
myCar1 = Car()
myCar1.color = "빨강"
myCar1.upSpeed(30)
print("자동차1의 색상은 %s이며, 현재 속도는 %d km입니다.\n생산된 자동차는 총 %d대입니다." % (myCar1.color, myCar1.speed, Car.count))

myCar2 = Car()
myCar2.color = "파랑"
myCar2.upSpeed(60)
print("자동차2의 색상은 %s이며, 현재 속도는 %d km입니다.\n생산된 자동차는 총 %d대입니다." % (myCar2.color, myCar2.speed, myCar2.count))

myCar3 = Car()
myCar3.color = "노랑"
myCar3.upSpeed(200)
print("자동차3의 색상은 %s이며, 현재 속도는 %d km입니다.\n생산된 자동차는 총 %d대입니다." % (myCar3.color, myCar3.speed, myCar3.count))

print("\n------------------------------\n")

# ------------------------------ #

## class 상속
    # 기존 class에 있는 필드와 메서드를 그대로 물려받는 새로운 class를 만드는 것
    # 공통된 내용을 자동차 class에 두고 상속받음으로써 일관되고 효율적인 프로그래밍 가능
    # 상위 class인 자동차 class를 '슈퍼 class'나 '부모 class'라 함
    # 하위 class인 승용차와 트럭 class는 '서브 class' 또는 '자식 class'라 함

    # 메서드 오버라이딩: 상위 class의 메서드를 서브 class에서 재정의하는 것

class Sedan(Car):
    def upSpeed(self, value):
        self.speed += value
        if self.speed > 150:
            self.speed = 150
        print("현재 속도(서브 class): %d km" % self.speed)

class Truck(Car):
    pass

sedan1, truck1 = None, None

truck1 = Truck()
sedan1 = Sedan()

print("트럭 --> ", end="")
truck1.upSpeed(200)

print("승용차 --> ", end="")
sedan1.upSpeed(200)

# ------------------------------ #

# 퍼셉트론 AND 구현
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

#
import numpy as np
x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7
print(w*x)
print(np.sum(w*x))
print(np.sum(w*x) + b) # 대략 -0.2 (부동소수점 수에 의한 연산 오차)

#
def numpyAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5]) # [-0.5, -0.5]로 바꾸면 NAND, [0.5, 0.5]로 바꾸면 OR로 기능
    b = -0.7 # 0.7로 바꾸면 NAND, -0.2로 바꾸면 OR로 기능
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1