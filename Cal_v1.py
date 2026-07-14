# 사칙연산 계산기 (나머지, 몫, 제곱 포함)

# 숫자 입력
num1 = float(input("첫 번째 숫자를 입력하세요: "))
operator = input("연산자를 입력하세요 (+, -, *, /, %, //, **): ")
num2 = float(input("두 번째 숫자를 입력하세요: "))

# 연산 수행
if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 == 0:
        print("0으로 나눌 수 없습니다.")
        result = None
    else:
        result = num1 / num2

elif operator == "%":
    if num2 == 0:
        print("0으로 나머지 연산을 할 수 없습니다.")
        result = None
    else:
        result = num1 % num2

elif operator == "//":
    if num2 == 0:
        print("0으로 몫 연산을 할 수 없습니다.")
        result = None
    else:
        result = num1 // num2

elif operator == "**":
    result = num1 ** num2

else:
    print("잘못된 연산자입니다.")
    result = None

# 결과 출력
if result is not None:
    print(f"결과: {result}")