"""
위장
문제 설명
스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.

예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴
코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란
안경 대신 검정 선글라스를 착용하거나 해야 합니다.

clothes	return
[[yellow_hat, headgear], [blue_sunglasses, eyewear], [green_turban, headgear]]	5
[[crow_mask, face], [blue_sunglasses, face], [smoky_makeup, face]]	3

뭐지? 그냥 묶은 다음에 (길이+1) * (길이2+1) - 1 하면 끝이잖아
"""
from functools import reduce


def solution(clothes):
    hash_dict = {}
    for clo in clothes:
        hash_dict.setdefault(clo[1], 0)
        hash_dict[clo[1]] += 1

    return reduce(lambda x, value: x * (value+1), hash_dict.values(), 1) - 1