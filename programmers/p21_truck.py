"""
트럭 여러 대가 강을 가로지르는 일 차선 다리를 *정해진 순*으로 건너려 합니다.
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다.
트럭은 1초에 1만큼 움직이며,
다리 길이는 bridge_length이고
다리는 무게 weight까지 견딥니다.
※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.
"""

from collections import deque

def solution(bridge_length, weight, truck_weights):
    clock = 0
    bridge = [0] * (bridge_length-1)
    want = len(truck_weights)
    now = 0
    while True:
        # 입구 심사
        if len(truck_weights) > 0 and truck_weights[0] <= weight:
            weight -= truck_weights[0]
            v = truck_weights.pop(0)
            bridge.append(v)
        else:
            bridge.append(0)
        print(bridge)

        # 출구 감시
        w = bridge.pop(0)
        if w != 0:
            now += 1
        weight += w

        clock += 1
        # 오늘 통행량 체크
        if now == want:
            break
    return clock+1
