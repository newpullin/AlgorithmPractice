def solution(brown, yellow):
    total = brown + yellow
    for W in range(3, int(total/3)+1):
        for H in range(3, W+1):
            if W*H == total:
                if 2*W + 2*H - 4 == brown:
                    return [W, H]

solution(8, 1)
# 이건 좀 쉽다