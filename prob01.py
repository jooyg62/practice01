# 문제1. 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요
import sys


def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


number = input('수를 입력하세요: ')

if(not isNumber(number)):
    print('정수가 아닙니다.')
    sys.exit(0)

number = int(number)

if number % 3:
    print('3의 배수가 아닙니다.')
    sys.exit(0) # 정상 종료
else:
    print('3의 배수 입니다.')
    sys.exit(0)  # 정상 종료



