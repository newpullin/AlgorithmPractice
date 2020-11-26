"""
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

제한사항
genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.
"""

# [classic, pop, classic, classic, pop]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]
# 장르별로 더하면서
# 장르끼리 묶으면서
# 순서를 정한다?
def solution(genres, plays):
    answer = []

    genres_count_dict = {}
    genres_index_list_dict = {}
    play_dict = {}
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]

        # Counting each genres with dictionary
        genres_count_dict.setdefault(g, 0)
        genres_count_dict[g] += p

        # save index and plays into list in dict[genres]
        genres_index_list_dict.setdefault(g, [])
        genres_index_list_dict[g].append((i, p))


    # sorting genres by total
    sorted_genres = sorted(genres_count_dict.keys(), key=(lambda x: genres_count_dict[x]), reverse=True)

    answer = []
    # print(sorted_genres)
    # append index ordered by genres
    for key_v in sorted_genres:
        target = genres_index_list_dict[key_v]
        if len(target) == 1:
            answer.append(target[0][0])
            continue
        # print(f"target : {target}")
        sorted_target = sorted(target, key=(lambda x: x[1]), reverse=True)
        # print(f"sorted target : {sorted_target}")
        #answer.extend([x[0] for x in sorted_target[:2]])
        answer.append(sorted_target[0][0])
        answer.append(sorted_target[1][0])

    return answer

"""
genres=[classic,classic,classic,classic,pop]
plays=[500,150,800,800,2500]
"""
#print(solution(["classic","classic","classic","classic","pop"], [500,150,800,800,2500])) # 4 2 3
print(solution(['A', 'A', 'B', 'A'], [5, 5, 6, 5])) # 0 1 2