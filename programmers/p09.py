
"""/*
print(solution(BBBAAAB))#9
print(solution(ABABAAAAABA)) #11
"""

import collections

def calcWay(c1, c2, max, func):
    way1 = func(c2) - func(c1)
    way2 = max - func(c2) + func(c1)
    return (way1, way2)




def solution(name):
    count = 0
    name = name.lower()
    diff = collections.deque([0])
    len_name = len(name)
    # change character
    for i, tc in enumerate(name):
        count += min(*calcWay('a', tc, 26, ord))
        if tc != 'a' and i != 0:
            diff.append(i)

    # cursor move
    if len(diff) == 1:
        return count
    else:
        while len(diff) != 0:
            poped = diff.popleft()

            left = diff[-1]
            right = diff[0]

            left_way = min(*calcWay(poped, left, len_name, lambda x: x))
            if left == right:
                count += left_way
                break
            right_way = min(*calcWay(poped, right, len_name, lambda x: x))

            if left_way < right_way:
                count += left_way
                diff.rotate(1)
            else:
                count += right_way

    return count

print(solution("JAN"))