def solution(scoville, K):
    scoville.sort()
    min_index = 0
    count = 0
    while scoville[min_index] < K:

        # 최솟값 2개를 이용하여 새로운 아이템을 만든다.
        new_item = scoville[min_index] + scoville[min_index+1] * 2
        count += 1
        min_index += 2
        if min_index == len(scoville):
            if new_item < K:
                return -1

        new_pos = min_index
        while scoville[new_pos] < new_item and new_pos < len(scoville)-1:
            new_pos += 1

        scoville.insert(new_pos, new_item)

    return count

scovile = [1, 2, 3, 9, 10, 12]

print(solution(scovile, 7))