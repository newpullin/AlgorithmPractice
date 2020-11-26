from itertools import permutations


def solution(number: str) -> int:
    n = len(number)
    possible = set(map(''.join, permutations(number)))
    max_value = int(max(possible))
    for i in range(1, n):
        possible.update(set(map(''.join, permutations(number, i))))
    #set 숫자로 변환
    possible = set(map(int, possible))
    eratos = [x for x in range(3, max_value+1, 2)]
    primes = []
    while len(eratos) > 0:
        v = eratos.pop(0)
        primes.append(v)
        eratos = [x for x in eratos if x % v != 0]

    count = 0
    for num in possible:
        if num == 2:
            count += 1
            continue

        if num % 2 == 0:
            continue

        if num in primes:
            count += 1

    return count


print(solution("7843"))