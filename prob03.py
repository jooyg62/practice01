# 문제3. 다음과 같은 출력이 되도록 이중 for~in 문을 사용한 코드를 작성하세요.
for i in range(0, 10): # in 다음으로는 시퀀스 형태만 가능
    for j in range(0, i):
        print('*', end='')
    print('')


