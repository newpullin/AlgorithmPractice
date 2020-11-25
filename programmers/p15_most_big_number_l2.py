""""
문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
"""


def solution(numbers):
    num_to_str = list(map(str, numbers))
    # 튜플로 만들어 인덱스와 만들어낸 값을 같이 저장할 필요 없이 정렬할 때  만들어낸 값을 기준으로 해버리면 훨씬 간단해진다.
    index_with_filled9 = [(index, int(s + (s*3)[0:(4 - len(s))])) for index, s in enumerate(num_to_str)]
    sorted_tuple = sorted(index_with_filled9, key=lambda x: x[1], reverse=True)
    answer = "".join([num_to_str[t[0]] for t in sorted_tuple])

    return str(int(answer))
