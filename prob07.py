# 문제 7. 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오
import sys


def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

data = []

for i in range(0, 5):
    number = input('정수를 입력하세요: ')

    if (not isNumber(number)):
        print('정수가 아닙니다.')
        sys.exit(0)

    number = int(number)

    data.append(number)

print('평균:', sum(data, 0.0)/len(data))

