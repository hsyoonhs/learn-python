# a, b = 100, 200
# print(a == b, a != b, a > b, a < b, a >= b, a <= b)

# ------------------------------ #

# print("A" < "a")
# print("325" > "323")
# print("323" >= "325")
# print("Abc" < "abc")
# print("Abc" <= "abc")
# print("ABC" == "ABC")
# print("ABC" != "ABC")

# print("325.5" < "326")
# print("abc" < "가나다")

# 😂 = U+1F602, 😍 = U+1F60D
# print("😂" < "😍")

# ------------------------------ #

# a = 99
# print((a > 100) and (a < 200), (a > 100) or (a < 200), not(a == 100))

# ------------------------------ #

# a = ord('A')
# mask = 0x0F

# print("%x & %x = %x" % (a, mask, a & mask)) # 0x41 & 0x0F
# print("%X | %X = %X" % (a, mask, a | mask))

# mask = ord('a') - ord('A')

# b = a ^ mask
# print("%c ^ %d = %c" % (a, mask, b))
# a = b ^ mask
# print("%c ^ %d = %c" % (b, mask, a))

# ------------------------------ #

# a = 10
# print(a << 1, a << 2, a << 3, a << 4)
# 10*2**1, 10*2**2, 10*2**3, 10*2**4

# a = 10
# print(a >> 1, a >> 2, a >> 3, a >> 4)
# 10//2**1, 10//2**2, 10//2**3, 10//2**4

# ------------------------------ #

# 1의 보수 뺄셈: 빼는 수에 대한 1의 보수를 구하고 더하기
# 자리올림이 발생하면 최하위 비트에 1을 더하고 자리올림된 비트는 제외
# 자리올림이 발생하지 않으면 결과에 대한 1의 보수를 구하고 마이너스(-) 부호 붙임

# 2의 보수 뺄셈: 빼는 수에 대한 2의 보수를 구하고 더하기
# 자리올림이 발생하면 자리올림된 비트는 제외
# 자리올림이 발생하지 않으면 결과에 대한 2의 보수를 구하고 마이너스(-) 부호 붙임

# ------------------------------ #

# print(0.1 + 0.1)
# print(0.1 + 0.2) # 0.30000000000000004
# print(0.1 + 0.3)
# print(0.1 + 0.4)
# print(0.1 + 0.5)
# print(0.1 + 0.6)
# print(0.1 + 0.7) # 0.7999999999999999
# print(0.1 + 0.8)
# print(0.1 + 0.9)

# ------------------------------ #

# a = 99
# if a < 100 :
#     print("100보다 작습니다.")
    
# a = 200
# if a < 100:
#     print("100보다 작습니다.")
# print("if 조건문 단락은 들여쓰기로 구분합니다.")
# print("프로그램 끝")

# a = 200
# if a < 100:
#     print("100보다 작습니다.")
#     print("if 조건문 단락은 들여쓰기로 구분합니다.")
# print("프로그램 끝")

# ------------------------------ #

# a = 200
# if a < 100:
#     print("100보다 작습니다.")
#     print("if 조건문에 대하여 참이면 이 문장이 보입니다.")
# else:
#     print("100보다 큽니다.")
#     print("if 조건문에 대하여 거짓이면 이 문장이 보입니다.")
# print("프로그램 끝")

# a = int(input(("정수를 입력하세요: ")))
# if a % 2 == 0:
#     print("짝수를 입력하셨습니다.")
# else:
#     print("홀수를 입력하셨습니다.")

# ------------------------------ #

# a = 75
# if a > 50:
#     if a < 100:
#         print("50 초과 100 미만의 값을 입력하셨습니다.")
#     else:
#         print("100 이상의 값을 입력하셨습니다.")
# else:
#     print("50 이하의 값을 입력하셨습니다.")

# ------------------------------ #

# score = int(input("점수를 입력하세요: "))
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# elif score >= 50:
#     print("E")
# else:
#     print("F")
# print("학점입니다.")

score = float(input("점수를 입력하세요: "))
if score >= 95:
    print("A+")
elif score >= 90:
    print("A0")
elif score >= 85:
    print("B+")
elif score >= 80:
    print("B0")
elif score >= 75:
    print("C+")
elif score >= 70:
    print("C0")
elif score >= 65:
    print("D+")
elif score >= 60:
    print("D0")
elif score >= 55:
    print("E+")
elif score >= 50:
    print("E0")
else:
    print("F")
print("학점입니다.")