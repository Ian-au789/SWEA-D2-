# https://married-spot-253.notion.site/IM-1-17a3cb37136a81538275c0d22b2be4ce?p=17a3cb37136a81b985abcddc8f9ca5bc&pm=s

# 제출용 답안
'''
cost = int(input())

# 금액의 각 자릿수 값을 저장할 변수
fifth_digit = 0
fourth_digit = 0
third_digit = 0
second_digit = 0

# 화폐 개수 저장할 변수
fifty_thousand = 0
ten_thousand = 0
five_thousand = 0
one_thousand = 0
five_hundred = 0
one_hundred = 0
fifty = 0
ten = 0

# 금액의 각 자릿수 값 계산
fifth_digit = cost // 10000

fourth_digit = (cost - fifth_digit*10000) // 1000

third_digit = (cost - fifth_digit*10000 - fourth_digit*1000) // 100

second_digit = (cost - fifth_digit*10000 - fourth_digit*1000 - third_digit*100) // 10

# 5만원권, 만원권 개수 계산
if fifth_digit >= 5:
    fifty_thousand = fifth_digit // 5
    ten_thousand = fifth_digit % 5

else:
    ten_thousand = fifth_digit

# 5천원권, 천원권 개수 계산
if fourth_digit >= 5:
    five_thousand = fourth_digit // 5
    one_thousand = fourth_digit % 5

else:
    one_thousand = fourth_digit

# 5백원, 백원 개수 계산
if third_digit >= 5:
    five_hundred = third_digit // 5
    one_hundred = third_digit % 5

else:
    one_hundred = third_digit

# 5십원, 십원 개수 계산
if second_digit >= 5:
    fifty = second_digit // 5
    ten = second_digit % 5

else:
    ten = second_digit

# print(f"#{test_case}")

print(f"{fifty_thousand} {ten_thousand} {five_thousand} {one_thousand} {five_hundred} {one_hundred})
'''

