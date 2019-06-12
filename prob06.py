# 문제6. 키보드에서 정수로 된 돈의 액수를 입력 받아
# 오만 원권, 만원 권, 오천 원권, 천원 권, 500원짜리 동전, 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전
# 각 몇 개로 변환 되는지 작성하시오.
import sys


def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


money = input('금액를 입력하세요: ')

if(not isNumber(money)):
    print('금액 정보가 맞지 않습니다.')
    sys.exit(0)

money = int(money)

remain_amount = money;

for won in [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]:
    result, last = divmod(remain_amount, won)
    remain_amount -= won * result
    print(str(won) + '원 : ' + str(result) + '개')


