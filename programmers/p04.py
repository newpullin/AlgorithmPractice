def getMiddle(a, b):
    return int((a + b) / 2)


def solution(n, times):
    best = 0
    worst = max(times) * n
    while best <= worst:
        mid = getMiddle(worst, best)
        sum = 0
        for t in times:
            sum += mid // t
        if sum >= n:
            worst = mid - 1
        elif sum < n:
            best = mid + 1


    return mid


print(solution(60000, [5, 7, 10, 12, 20]))