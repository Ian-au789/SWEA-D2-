# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVF-WqqecDFAWg# (색칠하기)

# 제출용 답안
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    row_input = []
    matrix_input = []

    for i in range(0, N):
        row_input = list(map(int, input().split()))
        matrix_input.append(row_input)

    def find_purple(input_list):
        red_area = []
        blue_area = []                                                      # 색깔에 따라 분류


        for list in input_list:
            four_points = []                           

            if list[4] == 1:                                                # list 마지막 값으로 색 판별
                list.pop()                                                  # 마지막 항목 제거
                four_points = list
                red_area.append(four_points)

            else:
                list.pop()
                four_points = list
                blue_area.append(four_points)


        coordinate1 = [[0]*10 for _ in range(10)]                           # 빨간색 표시할 좌표평면 
        coordinate2 = [[0]*10 for _ in range(10)]                           # 파란색 표시할 좌표평면 

        for list in red_area:
            for x_coor in range(list[0], list[2]+1):
                for y_coor in range(list[1], list[3]+1):
                    coordinate1[x_coor][y_coor] = 1                         # 빨간 영역에 1 할당

        for list in blue_area:
            for x_coor in range(list[0], list[2]+1):
                for y_coor in range(list[1], list[3]+1):
                    coordinate2[x_coor][y_coor] = 2                         # 파란 영역에 2 할당

        purple = 0

        for x in range(0, 10):
            for y in range(0, 10):
                if coordinate1[x][y] + coordinate2[x][y] == 3:              #빨간색과 파란색이 겹치는 지점 탐색
                    purple += 1

        return purple
    
    
    result = find_purple(matrix_input)
    
    print(f"#{test_case} {result}")
'''

N = 2
matrix_input = [[1, 2, 3, 3, 1], [3, 6, 6, 8, 1], [2, 3, 5, 6, 2]]

def find_purple(input_list):
    red_area = []
    blue_area = []                                                      # 색깔에 따라 분류


    for list in input_list:
        four_points = []                           

        if list[4] == 1:                                                # list 마지막 값으로 색 판별
            list.pop()                                                  # 마지막 항목 제거
            four_points = list
            red_area.append(four_points)

        else:
            list.pop()
            four_points = list
            blue_area.append(four_points)


    coordinate1 = [[0]*10 for _ in range(10)]                           # 빨간색 표시할 좌표평면 
    coordinate2 = [[0]*10 for _ in range(10)]                           # 파란색 표시할 좌표평면 

    for list in red_area:
        for x_coor in range(list[0], list[2]+1):
            for y_coor in range(list[1], list[3]+1):
                coordinate1[x_coor][y_coor] = 1                         # 빨간 영역에 1 할당

    for list in blue_area:
        for x_coor in range(list[0], list[2]+1):
            for y_coor in range(list[1], list[3]+1):
                coordinate2[x_coor][y_coor] = 2                         # 파란 영역에 2 할당

    purple = 0

    for i in range(0, 10):
        for j in range(0, 10):
            if coordinate1[i][j] + coordinate2[i][j] == 3:              #빨간색과 파란색이 겹치는 지점 탐색
                purple += 1
    
    return purple

print(find_purple(matrix_input))