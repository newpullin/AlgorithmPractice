prices = [1, 2, 3, 2, 3]

def solution(prices):
    answer = [0] * len(prices)
    # 마지막은 다음 값이 없으므로 무조건 0 초이다.
    answer[-1] = 0
    # 마지막에서 2번째는 떨어져도 1초, 올라도 1초이므로 무조건 1초이다.
    answer[-2] = 1
    # 끝에서 3번째 부터 거꾸로 찾아간다. (이전에 찾은 거리값을 활용하기위하여)
    for index in range(len(prices)-3,-1,-1):
        searching = 1
        while True:
            # 만약 자신보다 작은 값을 찾았다면 그 거리를 기록하고 종료
            if prices[index] > prices[index+searching]:
                answer[index] = searching
                break
            else:
                searching += answer[index+searching]
                # 만약 거리값이 0 이라면 끝에 도달하였으므로 종료
                if answer[index+searching] == 0:
                    answer[index] = searching
                    break

    return answer


print(solution(prices))