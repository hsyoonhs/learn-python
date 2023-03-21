# a = (100==100)
# b = (10>100)

# print(a,b)

# ------------------------------ #

# one = True
# two = False

# print(
#     type(one),
    
#     not one,
    
#     one and two,
    
#     one or two
# )

# ------------------------------ #

# print("Life is too short. You need python\nLife is too short.\nYou need python.")

# or

# print("Life is too short. You need python")
# print("Life is too short.\nYou need python.")

# ------------------------------ #

# print("    *    \n   ***   \n  *****  \n ******* \n*********\n ******* \n  ***** \n   ***   \n    *    ")

# ------------------------------ #

# str_input = input("원의 반지름 입력> ")

# num_input = float(str_input)

# print()
# print("반지름:", num_input)
# print("둘레:", 2*3.14*num_input)
# print("넓이:", 3.14*num_input**2)

# ------------------------------ #

# first = int(input("첫 번째 숫자를 입력하세요: "))
# second = int(input("두 번째 숫자를 입력하세요: "))

# print("%s + %s = %s" % (first, second, first+second))
# print("%s - %s = %s" % (first, second, first-second))
# print("%s * %s = %s" % (first, second, first*second))
# print("%s / %s = %s" % (first, second, first/second))

# or

# first = int(input("첫 번째 숫자를 입력하세요: "))
# second = int(input("두 번째 숫자를 입력하세요: "))

# print(first, "+", second, "=", (first+second))
# print(first, "-", second, "=", (first-second))
# print(first, "*", second, "=", (first*second))
# print(first, "/", second, "=", (first/second))

# or

# first = int(input("첫 번째 숫자를 입력하세요: "))
# second = int(input("두 번째 숫자를 입력하세요: "))

# result = first+second
# print(first, "+", second, "=", result)

# result = first-second
# print(first, "-", second, "=", result)

# result = first*second
# print(first, "*", second, "=", result)

# result = first/second
# print(first, "/", second, "=", result)

# ------------------------------ #

# num_input = int(input("정수를 입력하세요: "))
# print("구구단 %s단" % num_input)
# print("------------")
# print(num_input, "x 1 =", num_input)
# print(num_input, "x 2 =", num_input*2)
# print(num_input, "x 3 =", num_input*3)
# print(num_input, "x 4 =", num_input*4)
# print(num_input, "x 5 =", num_input*5)
# print(num_input, "x 6 =", num_input*6)
# print(num_input, "x 7 =", num_input*7)
# print(num_input, "x 8 =", num_input*8)
# print(num_input, "x 9 =", num_input*9)

# ------------------------------ #

# a = 5; b = 3
# # a, b = 5, 3
# print(a+b, a-b, a*b, a/b, a//b, a%b, a**b)

# ------------------------------ #

# print(1 + 2)
# print("1" + "2")
# print("전공SW기초 " + "수업은 " + "파이썬으로!")
# print("전공SW기초 " + "수업은 " + "파이썬으로!" * 2)

# ------------------------------ #

# s1, s2, s3 = "100", "100.123", "999999999999999999999999999999"
# print(int(s1) + 1, float(s2) + 1, int(s3) + 1)

# ------------------------------ #

# a = 100; b = 100.123
# print(str(a) + "1", str(b) + "1")

# ------------------------------ #

# a = 10
# a += 5; print(a)
# a -= 5; print(a)
# a *= 5; print(a)
# a /= 5; print(a)
# a //= 5; print(a)
# a %= 5; print(a)
# a **= 5; print(a)

# ------------------------------ #

# 변수 선언
money, c500, c100, c50, c10 = 0, 0, 0, 0, 0

# 주
money = int(input("교환할 돈은 얼마? "))

c500 = money // 500
money %= 500

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10

# print()
# print("500원짜리 ==> %s개" % c500)
# print("100원짜리 ==> %s개" % c100)
# print("50원짜리 ==> %s개" % c50)
# print("10원짜리 ==> %s개" % c10)
# print("바꾸지 못한 잔돈 ==> %s원" % money)

# %s 대신 %d를 사용할 수 있음

# or

print()
print("500원짜리 ==> " + str(c500) + "개")
print("100원짜리 ==> " + str(c100) + "개")
print("50원짜리 ==> " + str(c50) + "개")
print("10원짜리 ==> " + str(c10) + "개")
print("바꾸지 못한 잔돈 ==> " + str(money) + "개")