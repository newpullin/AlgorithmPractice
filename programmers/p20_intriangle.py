def solution(triangle):
    for r_i, row in enumerate(triangle):
        if r_i == 0:
            continue
        for c_i, col in enumerate(row):
            left_value = -1
            if c_i >= 1:
                left_value = triangle[r_i-1][c_i-1]
            right_value = -1
            if c_i < r_i:
                right_value = triangle[r_i - 1][c_i]

            triangle[r_i][c_i] += max(left_value, right_value)
    
    return max(triangle[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))