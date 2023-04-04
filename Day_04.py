# 날짜/시간 관련 기능 가져오기
# import datetime

# 현재 날짜/시간 구하기
# now = datetime.datetime.now();

# 결과 출력 1
# print(now.year, "년")
# print(now.month, "월")
# print(now.day, "일")
# print(now.hour, "시")
# print(now.minute, "분")
# print(now.second, "초")

# 결과 출력 2
# print("{}년 {}월 {}일 {}시 {}분 {}초".format(
#     now.year,
#     now.month,
#     now.day,
#     now.hour,
#     now.minute,
#     now.second
# ))

# 결과 출력 3
# if now.hour <= 12:
#     print("현재 시각은 오전 {}시입니다.".format(now.hour))
# if now.hour > 12:
#     print("현재 시각은 오후 {}시입니다.".format(now.hour - 12))

# 결과 출력 4
# if 3 <= now.month <= 5:
#     print("이번 달은 {}월, 봄입니다.".format(now.month))
# if 6 <= now.month <= 8:
#     print("이번 달은 {}월, 여름입니다.".format(now.month))
# if 9 <= now.month <= 11:
#     print("이번 달은 {}월, 가을입니다.".format(now.month))
# if 12 == now.month or 1 <= now.month <= 2:
#     print("이번 달은 {}월, 여름입니다.".format(now.month))

# ------------------------------ #

# balance = 1000000

# Withdraw = int(input("출금할 금액을 입력해주세요. "))

# if Withdraw <= 0:
#     print("잘못된 출금액입니다. 다시 입력해주세요.")
# elif balance < Withdraw:
#     print("출금액이 잔고보다 큽니다. (잔고 부족)")
# else:
#     balance -= Withdraw
#     print("{}원을 출금했습니다.".format(Withdraw))

# print("현재 잔고는 {}원입니다.".format(balance))

# ------------------------------ #

# 방식 1
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     print(num)
# print("반복문 종료")

# 방식 2, range 활용
# numbers = range(10)
# for num in numbers:
#     print(num + 1)
# print("반복문 종료")

# ------------------------------ #

# for i in [0, 1, 2]:
#     print("문구")

# for i in range(0, 3, 1):
#     print("문구")

# for i in range(0, 3, 1):
#     print("%d. 문구" % i)
    
# for i in range(1, 6, 1):
#     print("%d " % i, end = "")

# for i in range(2, -1, -1):
#     print("%d. 문구" % i)

# ------------------------------ #

# totalsum = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# print("1에서 10까지 합계: %d" % totalsum)

# i, totalsum = 0, 0
# for i in range(1, 11, 1):
#     totalsum += i
# print("1에서 10까지 합계: %d" % totalsum)

# i, totalsum = 0, 0
# for i in range(501, 1001, 2):
#     totalsum += i
# print("500과 1000 사이에 있는 홀수의 합계: %d" % totalsum)

# i, totalsum = 0, 0
# for i in range(0, 101, 7):
#     totalsum += i
# print("0과 100 사이에 있는 7의 배수의 합계: %d" % totalsum)

# ------------------------------ #

# i, totalsum = 0, 0
# num = int(input("값을 입력하세요: "))

# if num <= 1:
#     print("입력값은 1보다 커야 합니다.")
# else:
#     for i in range(1, num + 1, 1):
#         totalsum += i
#     print("1에서 {}까지의 합계: {}".format(num, totalsum))

# ------------------------------ #

# i, totalsum = 0, 0
# startNum = int(input("시작값을 입력하세요: "))
# endNum = int(input("끝값을 입력하세요: "))
# increNum = int(input("증가값을 입력하세요: "))

# if endNum <= startNum:
#     print("끝값은 시작값보다 커야 합니다.")
# else:
#     for i in range(startNum, endNum + 1, increNum):
#         totalsum += i
#     print("{}에서 {}까지 {}씩 증가시킨 값의 합계: {}".format(startNum, endNum, increNum, totalsum))

# ------------------------------ #

# i, times = 0, 0
# times = int(input("구구단 단수를 입력하세요: "))

# for i in range(1, 10, 1):
#     print("%d × %d = %2d" % (times, i, times * i))

# ------------------------------ #

# for i in range(0, 3, 1):
#     for k in range(0, 2, 1):
#         print("문구 (i: %d, k: %d)" % (i, k))

# ------------------------------ #

# i, k = 0, 0
# for i in range(2, 10, 1):
#     print("구구단 %d단\n----------" % i)
#     for k in range(1, 10, 1):
#         print("%d × %d = %2d" % (i, k, i * k))
#     print("")

# ------------------------------ #

i, k = 0, 0
for i in range(2, 10, 1):
    print(" -- %d단 -- | " % i, end="")

print("")

for j in range(1, 10, 1):
    for k in range(2, 10, 1):
        print("%d × %d = %2d | " % (j, k, j * k), end="")
    print("")