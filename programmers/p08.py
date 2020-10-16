def solution(numbers, target):
    pm = [0] * len(numbers)
    answer = recur(pm, numbers, target)

    return answer


def recur(pm, numbers, target):
    end = True
    count = 0
    for index, i in enumerate(pm):
        if i == 0:
            end = False
            new_pm1 = pm.copy()
            new_pm2 = pm.copy()
            new_pm1[index] = -1
            new_pm2[index] = 1
            count += recur(new_pm1, numbers, target)
            count += recur(new_pm2, numbers, target)
            break

    if end:
        result = 0

        for i in range(len(numbers)):
            result += pm[i]*numbers[i]

        if result == target:
            print(pm, result)
            return 1
        else:
            return 0

    return count

print(solution([1, 1, 1, 1, 1], 3))