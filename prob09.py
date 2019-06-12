# 문제9. 주어진 if 문을 dict를 사용해서 수정하세요.
menu = input('메뉴: ')

dic = {'오뎅':'300', '순대':'400', '만두':'500'}

if menu in dic:
    print('가격:', dic[menu])
else:
    print('가격:', 0)
