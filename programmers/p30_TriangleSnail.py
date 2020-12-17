from functools import reduce


def solution(n):
    triangle = [[0 for _ in range(x)] for x in range(1, n+1)]
    pos = [0, -1]
    # direction = ['down', 'right', 'up']
    direct_index = 0
    count = 1
    for x in range(n, 0, -1):
        for i in range(x):
            if direct_index == 0:
                pos[1] += 1
            elif direct_index == 1:
                pos[0] += 1
            else:
                pos[0] -= 1
                pos[1] -= 1
            triangle[pos[1]][pos[0]] = count
            count += 1

        direct_index = (direct_index + 1) % 3

    return list(reduce(lambda x, y: x+y, triangle))


print(solution(6))