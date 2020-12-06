#
# 대각선을 탐색하면서 자신이 물 웅덩이가 아니면
# 왼쪽이나 위쪽에서, 땡겨온다.
# 1,000,000,007로 나눈 나머지 %

def in_range(x, y, max_x, max_y):
    if (0 <= x < max_x) and (0 <= y < max_y):
        return True
    return False


def solution(m, n, puddles):
    map_array = [[-1 for _ in range(m)] for _ in range(n)]

    # 웅덩이 생성
    for puddle in puddles:
        map_array[puddle[1]-1][puddle[0]-1] = 0

    # 대각선 경로를 저장 ////
    diagonal_path = []
    for x_i in range(1, m):
        for y_i in range(x_i+1):
            # 범위 안에 있거나 웅덩이가 아니면 경로에 추가가
            if in_range(x_i, y_i, m, n) and map_array[y_i][x_i - y_i] != 0:
                 diagonal_path.append((x_i - y_i, y_i))
    for y_i in range(1, n):
        for x_i in range(n-y_i):
            if in_range(x_i, y_i, m, n) and map_array[y_i + x_i][m-1-x_i] != 0:
                diagonal_path.append((m-1-x_i, y_i + x_i))

    # 시작 지점은 1
    map_array[0][0] = 1

    for x_i, y_i in diagonal_path:
        # -1로 되어 있는거 0으로
        map_array[y_i][x_i] += 1
        # 왼쪽에서 끌어오기
        if x_i > 0:
            map_array[y_i][x_i] += map_array[y_i][x_i-1]
        # 오른쪽에서 끌어오기
        if y_i > 0:
            map_array[y_i][x_i] += map_array[y_i-1][x_i]

        map_array[y_i][x_i] %= 1_000_000_007

    return map_array[n-1][m-1] % 1_000_000_007

print(solution(4, 3, [[2, 2]]))