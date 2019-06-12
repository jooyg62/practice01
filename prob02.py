# 문제2. 키보드로 정수 수치를 입력 받아 짝수인지 홀수 인지 판별하는 코드를 작성하세요.

number = input('수를 입력하세요: ')

number = int(number)

if number % 2:
    print('홀수')
else:
    print('짝수')
