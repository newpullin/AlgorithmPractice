
def solution(n, lost, reserve):
    order = [0, -1, 1]
    answer = n - len(lost)
    lost.sort()
    for o in order:
        for l in lost:
            if len(reserve) == 0 :
                break
            if (l+o) in reserve:
                reserve.remove(l+o)
                answer += 1
                break
    return answer