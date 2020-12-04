"""/*
print(solution(BBBAAAB))#9
print(solution(ABABAAAAABA)) #11
"""

def calcWay(c1, c2, max_v, func):
    way1 = func(c2) - func(c1)
    way2 = max_v - func(c2) + func(c1)
    return way1, way2


def left_move(now, move, max_v):
    next_pos = now - move
    if next_pos < 0:
        next_pos += max_v
    return next_pos


def right_move(now, move, max_v):
    next_pos = now + move
    if next_pos >= max_v:
        next_pos -= max_v
    return next_pos


def solution(name):
    # 문자를 바꿔야 하는 횟수를 구한다.
    up_down_count = 0

    target = []
    for i, c in enumerate(name):
        if c == 'A':
            continue
        up_down_count += min(calcWay('A', c, 26, ord))
        if i != 0:
            target.append(i)

    # 이동해야 하는 거리를 구한다

    left_right_count = 0
    start_pos = 0
    max_l = len(name)
    di = 'r'

    while len(target) > 0:
        l_m = 0
        r_m = 0
        for i_l in range(0, max_l):
            if left_move(start_pos, i_l, max_l) in target:
                l_m = i_l
                break

        for i_r in range(0, max_l):
            if right_move(start_pos, i_r, max_l) in target:
                r_m = i_r
                break

        if l_m < r_m or ((l_m == r_m) and (di == 'l')):
            left_right_count += l_m
            start_pos = left_move(start_pos, l_m, max_l)
            target.remove(start_pos)
            di = 'l'
        elif l_m > r_m or ((l_m == r_m) and (di == 'r')):
            left_right_count += r_m
            start_pos = right_move(start_pos, r_m, max_l)
            target.remove(start_pos)
            di = 'r'

    return left_right_count + up_down_count

print(solution("BBBAAAB"))
