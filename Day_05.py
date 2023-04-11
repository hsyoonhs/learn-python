# i, sum = 0, 0

# for i in range(501, 1000, 2):
#     sum += i

# print("500과 1000 사이에 있는 홀수의 합계: %d" % sum)

# ------------------------------ #

# i, sum = 0, 0

# for i in range(0, 101, 7):
#     sum += i

# print("500과 1000 사이에 있는 홀수의 합계: %d" % sum)

# ------------------------------ #

# i, sum = 0, 0

# num = int(input("값을 입력하세요: "))

# for i in range(1, (num + 1), 1):
#     sum += i

# print("1과 %d 사이에 있는 홀수의 합계: %d" % (num, sum))

# ------------------------------ #

# i, sum = 0, 0

# startnum = int(input("시작값을 입력하세요: "))
# endnum = int(input("끝값을 입력하세요: "))
# increnum = int(input("증가값을 입력하세요: "))

# for i in range(startnum, (endnum + 1), increnum):
#     sum += i

# print("%d에서 %d까지 %d씩 증가시킨 값의 합계: %d" % (startnum, endnum, increnum, sum))

# ------------------------------ #

# i, sum = 0, 0

# startnum = int(input("*** 첫 번째 숫자를 입력하세요: "))
# endnum = int(input("*** 마지막 번째 숫자를 입력하세요: "))
# increnum = int(input("*** 더할 숫자의 간격을 입력하세요: "))

# for i in range(startnum, (endnum + 1), increnum):
#     sum += i

# print("%d + %d + ... + %d(은)는 %d 입니다." % (startnum, (startnum + increnum), endnum, sum))

# ------------------------------ #

# 교재와 다른 방식으로 해결

# for i in range(9, 1, -1):
#     print("# %d단 #      " % i, end="")

# print("")

# for i in range(9, 1, -1):
#     for j in range(9, 1, -1):
#         print("%d × %d = %2d | " % (i, j, i*j), end="")
#     print("")

# ------------------------------ #

# 교재의 방식으로 해결

# ------------------------------ #

# i, answer = 0, 0.0

# selectNum = int(input("1. 입력한 수식 계산 | 2. 두 수 사이의 합계: "))

# if selectNum == 1:
#     expressionInput = input("*** 수식을 입력하세요: ")
#     answer = eval(expressionInput)
#     print("%s의 결과는 %0.1f입니다." % (expressionInput, answer))
# elif selectNum == 2:
#     firstNumInput = int(input("*** 첫 번째 숫자를 입력하세요: "))
#     lastNumInput = int(input("*** 마지막 숫자를 입력하세요: "))
#     for i in range(firstNumInput, (lastNumInput + 1), 1):
#         answer += i
#     print("%d + ... + %d는 %d입니다." % (firstNumInput, lastNumInput, answer))
# else:
#     print("1과 2 중에서 선택해야 합니다.")

# ------------------------------ #

# i = 0

# while i < 3:
#     print("%d: 안녕하세요? while문을 공부하는 중입니다." % i)
#     i += 1

# ------------------------------ #

# i, total = 0, 0

# while i < 11:
#     total += i
#     i += 1

# print("1에서 10까지의 합계: %d" % total)

# ------------------------------ #

# 수정 필요

# i, total = 0, 0

# startNum = int(input("시작값을 입력하세요: "))
# endNum = int(input("끝값을 입력하세요: "))
# increNum = int(input("증가값을 입력하세요: "))

# while i < (endNum + 1):
#     total += i
#     i += increNum

# print("%d에서 %d까지 %d씩 증가시킨 값의 합계: %d" % (startNum, endNum, increNum, total))

# ------------------------------ #

# while True:
#     print("ㅁㄴㅇㄹ ", end="")

# ------------------------------ #

# 교재와 다른 방식으로 해결

# firstNum, secondNum, ch = 0, 0, ""

# def asdf():
#     print("%d %s %d = %d" % (firstNum, ch, secondNum, eval("%d %s %d" % (firstNum, ch, secondNum))))

# while True:
#     firstNum = int(input("계산할 첫 번째 수를 입력하세요: "))
#     secondNum = int(input("계산할 두 번째 수를 입력하세요: "))
#     ch = input("계산할 연산자를 입력하세요: ")

#     if (ch == "+") or (ch == "-") or (ch == "*") or (ch == "/") or (ch == "%") or (ch == "//") or (ch == "**"):
#         asdf()
#     else:
#         print("올바른 연산자를 입력하세요.")

# ------------------------------ #

# total = 0
# firstNum, secondNum = 0, 0

# while True:
#     firstNum = int(input("더할 첫 번째 수 입력: "))
#     if firstNum == 0:
#         break
#     secondNum = int(input("더할 두 번째 수 입력: "))
#     total = firstNum + secondNum
#     print("%d + %d = %d" % (firstNum, secondNum, total))

# print("반복문 탈출")

# ------------------------------ #

# firstNum, secondNum, ch = 0, 0, ""

# def asdf():
#     print("%d %s %d = %d" % (firstNum, ch, secondNum, eval("%d %s %d" % (firstNum, ch, secondNum))))

# while True:
#     firstNum = int(input("계산할 첫 번째 수를 입력하세요: "))
#     secondNum = int(input("계산할 두 번째 수를 입력하세요: "))
#     ch = input("계산할 연산자를 입력하세요: ")

#     if (ch == "+") or (ch == "-") or (ch == "*") or (ch == "/") or (ch == "%") or (ch == "//") or (ch == "**"):
#         asdf()
#     elif (ch == "$"):
#         break
#     else:
#         print("올바른 연산자를 입력하세요.")

# ------------------------------ #

# total, i = 0, 0
# i = 1

# while True:
#     total += i

#     if total >= 1000:
#         break

#     i += 1

# print("1 + ... + n의 값이 1000을 넘게 하는 최소의 정수 n: %d" % i)

# ------------------------------ #

# 수정 필요

total, i = 0, 0

while i < 101:
    i += 1
    if i % 3 == 0:
        continue

    total += i

print("3의 배수를 제외한 1부터 100까지의 합계: %d" % total)

# ------------------------------ #

# i, k = 0, 0

# while i < 9:
#     if i < 5:
#         k = 0
#         while (k < (4 - i)):
#             print("　", end= "")
#             k += 1
#         k = 0
#         while (k < (i * 2 + 1)):
#             print("\u2605", end="")
#             k += 1
#     else:
#        k = 0
#        while (k < (i - 4)):
#            print("　", end="")
#            k += 1
#        k = 0
#        while (k < ((9 - i) * 2 - 1)):
#            print("\u2605", end="")
#            k += 1
#     print()
#     i += 1