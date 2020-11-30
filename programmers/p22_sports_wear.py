"""
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다.
다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다.
학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로
뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.
예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다.
체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost,
여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

제한사항
전체 학생의 수는 2명 이상 30명 이하입니다.
체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다.
이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
"""


def remove_same(set1, set2):
    intersect = set1 & set2
    return (set1 - intersect), (set2 - intersect)


def solution(n, lost, reserve):
    # 여벌 가졌는데 도난 당한 사람 = 여벌 없는 도난 안 당한 사람
    lost, reserve = remove_same(set(lost), set(reserve))

    # 잃어버린 사람 기준 오른쪽에서 빌린다
    lost_right = set(map(lambda x: x+1, lost))
    lost_right, reserve = remove_same(lost_right, reserve)

    # 아직도 잃어버린 사람 기준 왼쪽에서 빌린다
    lost_left = set(map(lambda x: x-2, lost_right))
    lost_final, _ = remove_same(lost_left, reserve)

    # 아직도 잃어버린 사람을 빼주면 체육복을 가진 사람의 수
    return n-len(lost_final)

