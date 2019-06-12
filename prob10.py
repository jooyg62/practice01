# 문제10. 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.
number = input('숫자를 입력하세요: ')

number = int(number)

sum = 0

if not number % 2 :
    # 짝수라면
    for i in range(0, number+1) :
        if not i % 2 :
            sum += i
else:
    # 홀수라면
    for i in range(1, number+1) :
        if i % 2 == 1 :
            sum += i

print('결과 값 :', sum)
