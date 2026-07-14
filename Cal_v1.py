# 반복되는 사칙연산 계산기

print("=== 사칙연산 계산기 ===")

while True:

    # 숫자 입력
    num1 = float(input("\n첫 번째 숫자를 입력하세요: "))
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
            continue
        result = num1 / num2

    elif operator == "%":
        if num2 == 0:
            print("0으로 나머지 연산을 할 수 없습니다.")
            continue
        result = num1 % num2

    elif operator == "//":
        if num2 == 0:
            print("0으로 몫 연산을 할 수 없습니다.")
            continue
        result = num1 // num2

    elif operator == "**":
        result = num1 ** num2

    else:
        print("잘못된 연산자입니다.")
        continue

    # 결과 출력
    print(f"결과: {result}")

    # 계속할지 종료할지 선택
    answer = input("\n계속 계산하시겠습니까? (y/n): ")

    if answer.lower() == "n":
        print("계산기를 종료합니다.")
        break