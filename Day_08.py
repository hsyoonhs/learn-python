# 리스트와 문자열의 비교

aa = [10, 20, 30, 40, 50]
print(aa[0])
print(aa[1:3])
print(aa[3:])

ss = '파이썬가나'
print(ss[0])
print(ss[1:3])
print(ss[3:])

print(len(ss))

sslen = len(ss)
for i in range(0, sslen):
    print(ss[i] + '◆', end="")

# ------------------------------ #

print("")

sofun = '파이썬은완전재미있어요'

sofunlen = len(sofun)
for i in range(0, sofunlen):
    if (i % 2) == 0:
        print(sofun[i], end="")
    else:
        print('#', end="")

# ------------------------------ #

# inputText, outputText = '', ''
# count = 0

# inputText = input('문자열을 입력하세요: ')
# inputLen = len(inputText)

# for i in range(0, inputLen):
#     outputText += inputText[inputLen - (i + 1)]

# print('내용을 거꾸로 출력 --> %s' % outputText)

# ------------------------------ #

print("")

# 대소문자 등 변환

ss = 'Python is easy. 그래서 programming이 재미있습니다.'
print(ss.upper()) # 대문자화
print(ss.lower()) # 소문자화
print(ss.swapcase()) # 대소문자 전환
print(ss.title()) # 제목화

# ------------------------------ #

# 예상 결과와 다름, 검토 필요, 각 줄당 주석 필요

ss = '파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠. ^^'

print(ss.count('공부'))
print(
      ss.find('공부'),
      ss.rfind('공부'),
      ss.find('국민', 5),
      ss.find('없다')
      )
print(
      ss.index('공부'),
      ss.rindex('공부'),
      ss.index('공부', 5)
      )
print(
      ss.startswith('파이썬'),
      ss.startswith('파이썬', 10),
      ss.endswith('^^')
      )

# ------------------------------ #

# 교재와 다른 방식으로 해결함

# inputForBrackets, output = '', '';

# inputForBrackets = input('입력 문자열 ==> ')

# output = inputForBrackets

# if not(inputForBrackets.startswith('(')):
#     output = '(' + output

# if not(inputForBrackets.endswith(')')):
#     output += ')'

# print(output)

# ------------------------------ #

ss = '  파 이 썬  '
print(ss.strip()) # 좌우 공백 제거
print(ss.rstrip()) # 우측 공백 제거
print(ss.lstrip()) # 좌측 공백 제거

ss = '----파---이---썬----'
print(ss.strip('-'))
ss = '<<<파 << 이 >> 썬>>>'
print(ss.strip('<>'))

# ------------------------------ #

# 문자열 중간 공백 삭제

inStr = "  한글 Python 프로그래밍  "
outStr = ""

for i in range(0, len(inStr)):
    if inStr[i] != ' ':
        outStr += inStr[i]

print("원래 문자열 ==> " + "[" + inStr + "]")
print("공백 삭제 문자열 ==> " + "[" + outStr + "]")

# 응용: 공백을 없애고 거꾸로 출력하기?

# ------------------------------ #

inStr = "<<<파<<이>>썬>>>"
outStr = ""

for i in range(0, len(inStr)):
    if inStr[i] != '<' and inStr[i] != '>':
        outStr += inStr[i]

print("원래 문자열 ==> " + "[" + inStr + "]")
print("'<'와 '>' 삭제 문자열 ==> " + "[" + outStr + "]")