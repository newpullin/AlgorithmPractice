from collections import deque

def solution(people, limit):
    # 같이 못 타는 사람 처리
    min_weight = min(people)
    light_people = [x for x in people if x <= limit - min_weight]
    answer = len(people) - len(light_people)

    people_sorted = deque(sorted(light_people))

    while people_sorted:
        heavy = people_sorted.pop()
        answer += 1

        if not people_sorted:
            break
        # 무조건 제일 가벼운 사람을 제일 무거운 사람하고 태우면 된다는 걸
        # 몰라서 효율성 실패 했었음
        if heavy + people_sorted[0] <= limit:
            people_sorted.popleft()

    return answer


print(solution(	[10,20,30,40,50,60,70,80,90], 100))

""" 통과

테스트 1 〉	통과 (1.07ms, 10.4MB)
테스트 2 〉	통과 (0.27ms, 10.1MB)
테스트 3 〉	통과 (0.84ms, 10.4MB)
테스트 4 〉	통과 (0.99ms, 10.2MB)
테스트 5 〉	통과 (0.54ms, 10.4MB)
테스트 6 〉	통과 (0.20ms, 10.2MB)
테스트 7 〉	통과 (0.38ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.07ms, 10.3MB)
테스트 10 〉	통과 (0.90ms, 10.3MB)
테스트 11 〉	통과 (0.85ms, 10.2MB)
테스트 12 〉	통과 (0.73ms, 10.3MB)
테스트 13 〉	통과 (0.64ms, 10.3MB)
테스트 14 〉	통과 (0.29ms, 10.2MB)
테스트 15 〉	통과 (0.03ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (9.16ms, 11.2MB)
테스트 2 〉	통과 (2.43ms, 10.2MB)
테스트 3 〉	통과 (6.99ms, 10.9MB)
테스트 4 〉	통과 (2.55ms, 10.3MB)
테스트 5 〉	통과 (1.88ms, 10.3MB)

"""


""" 실패

테스트 1 〉	통과 (8.66ms, 10.3MB)
테스트 2 〉	통과 (0.24ms, 10.2MB)
테스트 3 〉	통과 (2.97ms, 10.2MB)
테스트 4 〉	통과 (4.25ms, 10.2MB)
테스트 5 〉	통과 (1.96ms, 10.3MB)
테스트 6 〉	통과 (0.46ms, 10.3MB)
테스트 7 〉	통과 (1.53ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.18ms, 10.2MB)
테스트 10 〉	통과 (4.68ms, 10.2MB)
테스트 11 〉	통과 (2.17ms, 10.3MB)
테스트 12 〉	통과 (1.80ms, 10.2MB)
테스트 13 〉	통과 (2.33ms, 10.2MB)
테스트 14 〉	통과 (0.27ms, 10.2MB)
테스트 15 〉	통과 (0.04ms, 10.2MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	통과 (36.34ms, 10.3MB)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	통과 (2.29ms, 10.3MB)
테스트 5 〉	통과 (1.89ms, 10.3MB)

"""