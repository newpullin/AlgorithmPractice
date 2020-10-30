
"""/*
print(solution(BBBAAAB))#9
print(solution(ABABAAAAABA)) #11
"""


def calcWay(c1, c2, max, func):
    way1 = func(c2) - func(c1)
    way2 = max - func(c2) + func(c1)
    return (way1, way2)


def solution(name):
    count = 0
    name = name.lower()
    diff = []

    # change character
    for i, tc in enumerate(name):
        count += min(*calcWay('a', tc, 26, ord))
        if i != 0 and tc != 'a':
            diff.append(i + 1)

    # cursor move
    if len(diff) == 1:
        count += min(*calcWay(0, diff[0], len(name), lambda x: x))
    elif len(diff) > 1:
        count += min(max(*calcWay(0, diff[0], len(name), lambda x: x)),
                     max(*calcWay(0, diff[-1], len(name), lambda x: x)))

    return count

print(solution('ABABAAAAABA'))