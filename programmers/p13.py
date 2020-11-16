"""
가장 먼 노드
문제 설명
n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

제한사항
노드의 개수 n은 2 이상 20,000 이하입니다.
간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.
"""

def find_path_length(y, x, map, n):
    if map[y][x] == -1:
        min_value = 100000000
        # y -> x로 가는 길을 모르면 y -> t -> x 로 가는 길이 있는지 찾아본다.
        for t in range(n):
            if y == t or x == t:
                continue
            if map[y][t] != -1:
                path = map[y][t] + find_path_length(y, x, map, n)

        return "최소 경로를 찾는다."
    else:
        return map[y][x]

def solution(n, edge):
    map = [[-1 for i in range(n)] for k in range(n)]
    for e in sorted(edge, key=lambda vert: vert[0]):
        map[e[0]-1][e[1]-1] = 1
        map[e[1] - 1][e[0] - 1] = 1

    for k in range(n):
        map[k][k] = 0
    print(map)
    for i in range(n):
        print(find_path_length(0, i, map, n))
    #print(map)
    answer = 0
    return answer

vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
solution(6, vertex)

