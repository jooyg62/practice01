# 문제5. 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.
data = {0, 9, 12, 15, 18, 21, 24, 71}

count = 0
sum = 0


for num in data:
    if num != 0 and num % 3 == 0:
        count += 1
        sum += num

print('주어진 리스트에서 3의 배수의 개수=>', count)
print('주어진 리스트에서 3의 배수의 합=>', sum)
