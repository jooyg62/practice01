# 문제8. 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.
def reverse(s):
    result = '';

    for i in range(0, len(s)):
        result += s[len(s)-i-1:len(s)-i]

    return result


input_str = input('입력> ')

reverse_str = reverse(input_str)

print('결과>', reverse_str)
