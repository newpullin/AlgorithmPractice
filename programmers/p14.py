def generator(p1: int, p2: int, op) :
    if op == '+':
        return p1 + p2
    elif op == '-':
        return p1 - p2
    elif op == '*':
        return p1 * p2
    elif op == '/':
        return p1 // p2


operators = ['+', '-', '*', '/']

def solution(N, number):

    sets = []

    for i in range(1, 8+1):
        repeat = int(str(N)*i)
        if repeat == number:
            return i
        new_set = {repeat}
        for k in range(1, i):
            target1 = sets[k-1]
            target2 = sets[i-k-1]
            for t1 in target1:
                for t2 in target2:
                    for op in operators:
                        result = generator(t1, t2, op)
                        if result == number:
                            return i
                        # 이게 맞는건가?
                        if result > 0:
                            new_set.add(result)

        sets.append(new_set.copy())
    print(sets)
    return -1


# N num return
# 5 12 4
# 2 11 3

print(solution(2, 11))

"""
result != 0
테스트 1 〉	통과 (0.64ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.05ms, 10.4MB)
테스트 4 〉	통과 (36.93ms, 11.9MB)
테스트 5 〉	통과 (10.01ms, 10.5MB)
테스트 6 〉	통과 (0.29ms, 10.4MB)
테스트 7 〉	통과 (0.29ms, 10.3MB)
테스트 8 〉	통과 (15.67ms, 11.3MB)
테스트 9 〉	통과 (0.03ms, 10.4MB)
"""

"""
result > 0
테스트 1 〉	통과 (0.51ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.3MB)
테스트 4 〉	통과 (20.48ms, 11.6MB)
테스트 5 〉	통과 (6.07ms, 10.4MB)
테스트 6 〉	통과 (0.24ms, 10.4MB)
테스트 7 〉	통과 (0.23ms, 10.4MB)
테스트 8 〉	통과 (9.16ms, 10.5MB)
테스트 9 〉	통과 (0.03ms, 10.5MB)
"""

# 0이 포함 안되는 이유는 더해도 빼도 곱해도 나눠도 새로운 경우의 수를 만드는데 도움이 안됨
# < 0 이 포함 안되는 이유는? 일단 number가 양수라서 <0 이라면 <0로 곱해줘야 됨, 양수랑 대칭인데
# 굳이 마이너스로 만들어서 마이너스로 곱해줄 필요가 없으니까.