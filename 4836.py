# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVF-WqqecDFAWg# (색칠하기)

# 제출용 답안
'''
N = int(input())
row_list = []
matrix_list = []

for i in range(0, N):
    row_list = list(map(int, input(),split()))
    matrix_list.append(row_list)

'''
# [(list[0], list[2]), (list[0], list[3]), (list[1], list[2]), (list[1], list[3])]

N = 2
matrix_input = [[2, 2, 4, 4, 1], [3, 3, 6, 6, 2]]                  # [[1, 2, 3, 3, 1], [3, 6, 6, 8, 1], [2, 3, 5, 6, 2]]


red_area = []
blue_area = []


for list in matrix_input:
    four_points = []                           

    if list[4] == 1:                                                # list 마지막 값으로 색 판별
        four_points = [list[0], list[1], list[2], list[3]]
        red_area.append(four_points)

    else:
        four_points = [list[0], list[1], list[2], list[3]]
        blue_area.append(four_points)


