from collections import deque


def solution(routes):
    sorted_routes = deque(sorted(routes, key=lambda x: x[1]))

    camera_pos = sorted_routes.popleft()[1]
    answer = 1
    while sorted_routes:
        while sorted_routes and sorted_routes[0][0] <= camera_pos:
            sorted_routes.popleft()
        if sorted_routes:
            camera_pos = sorted_routes.popleft()[1]
            answer += 1
        else:
            break

    return answer


print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))