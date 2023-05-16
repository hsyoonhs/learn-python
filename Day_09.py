## 강의 내용 일부 생략됨

# ------------------------------ #

# 잘못됨

# inp = input("날짜(연/월/일) 입력 ==> ")
# inpList = inp.split("/")

# print("입력한 날짜의 10년 후 ==> ", end="")
# print(str((int(inp[0]) + 10)) + "년", end="")
# print(inp[1] + "월", end="")
# print(inp[2] + "일")

# ------------------------------ #

# 문자열 판단

# str = input("문자열 입력: ")

# if str.isdigit():
#     print("숫자입니다.")
# elif str.isalpha():
#     print("알파벳입니다.")
# elif str.isalnum():
#     print("알파벳과 숫자의 조합입니다.")
# else:
#     print("모르겠습니다.")

# ------------------------------ #

## 사용자 정의 함수 알아보기

# 전역 변수 선언
coffee = 0

# 함수 선언
def coffee_machine(button):
    print()
    print("#1 뜨거운 물을 준비한다.")
    print("#2 종이컵을 준비한다.")
    
    print("#3 ", end="")
    if coffee == 1:
        print("보통 커피를 탄다.")
    elif coffee == 2:
        print("설탕 커피를 탄다.")
    elif coffee == 3:
        print("설탕 커피를 탄다.")
    else:
        print("아무 커피나 탄다.")
    
    print("#4 물을 붓는다.")
    print("#5 스푼으로 젓는다.")
    print()

# 주 코드
# coffee = int(input("A손님, 어떤 커피 드릴까요?(1:보통, 2:설탕, 3:블랙) "))
# coffee_machine(coffee)
# print("손님~ 커피 여기 있습니다.")

# coffee = int(input("B손님, 어떤 커피 드릴까요?(1:보통, 2:설탕, 3:블랙) "))
# coffee_machine(coffee)
# print("손님~ 커피 여기 있습니다.")

# coffee = int(input("C손님, 어떤 커피 드릴까요?(1:보통, 2:설탕, 3:블랙) "))
# coffee_machine(coffee)
# print("손님~ 커피 여기 있습니다.")

# ------------------------------ #

def plus(v1, v2):
    result = 0
    result = v1 + v2
    return result

hap = 0

hap = plus(100, 200)
print("100과 200의 plus() 함수 결과는 %d" % hap)

# ------------------------------ #

def calc(v1, v2, op):
    result = 0

    if op == "+":
        result = v1 + v2
    elif op == "-":
        result = v1 - v2
    elif op == "*":
        result = v1 * v2
    elif op == "/":
        result = v1 / v2
    elif op == "**":
        result = v1 ** v2

    return result

res = 0
var1, var2, oper = 0, 0, ""

# var1 = int(input("첫 번째 수를 입력하세요: "))
# oper = input("연산자를 입력하세요(+, -, *, /, **): ")
# var2 = int(input("두 번째 수를 입력하세요: "))

if oper == "/" and var2 == 0:
    print("0으로는 나누면 안 됩니다.")
else:
    res = calc(var1, var2, oper)
    print("## 계산기: %d %s %d = %d" % (var1, oper, var2, res))

# ------------------------------ #

# 전역 변수 Global variable: 프로그램 전체에서 사용
# 지역 변수 Local variable: 한정된 지역에서만 사용

# ------------------------------ #

def func1():
    global a # 이 함수 안에서 a는 전역 변수
    a = 10
    print("func1()에서의 a 값: %d" % a)

def func2():
    print("func2()에서의 a 값: %d" % a)

a = 20 # 전역 변수

func2()
func1() # func1()과 func2()의 호출 순서를 달리하면 출력 결과가 바뀐다.

# ------------------------------ #

def multi(v1, v2):
    retList = []
    res1 = v1 + v2
    res2 = v1 - v2
    retList.append(res1)
    retList.append(res2)
    return retList

# 후반 생략됨

# ------------------------------ #

# 매개변수 전달

def para2_func(v1, v2):
    result = 0
    result = v1 + v2
    return result

def para3_func(v1, v2, v3):
    result = 0
    result = v1 + v2 + v3
    return result

hap = 0

hap = para2_func(10, 20)
print("매개변수가 2개인 함수를 호출한 결과 ==> %d" % hap)
hap = para3_func(10, 20, 30)
print("매개변수가 3개인 함수를 호출한 결과 ==> %d" % hap)