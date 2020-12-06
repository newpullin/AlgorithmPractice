def solution(routes):
    sorted_routes = sorted(routes, key=lambda x: x[1])

    camera_pos = -30000
    answer = 0
    for route in sorted_routes:
        # 설치된 카메라 위치보다 왼쪽에 있으면 패스
        # 입구가 설치된 카메라 위치보다 오른쪽에 있으면 카메라 위치는 출구
        if route[0] > camera_pos:
            camera_pos = route[1]
            answer += 1

    return answer


print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))