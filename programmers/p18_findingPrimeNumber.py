from itertools import permutations
import math

def solution(number: str) -> int:
    n = len(number)
    possible = set(map(''.join, permutations(number)))

    for i in range(1, n):
        possible.update(set(map(''.join, permutations(number, i))))
    #set 숫자로 변환
    possible = set(map(int, possible))

    # 1제거
    if 1 in possible:
        possible.remove(1)

    count = 0
    for num in possible:
        if num == 2:
            count += 1
            continue

        if num % 2 == 0:
            continue

        prime = True
        for i in range(3, int(math.sqrt(num)+1), 2):
            if num % i == 0:
                prime = False
                break

        if prime:
            count += 1
    return count


print(solution("011"))