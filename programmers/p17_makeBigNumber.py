def solution(number, k):
    number_i = list(map(int, number))
    number_len = len(number_i)
    # 왕을 뽑습니다.
    king = 9
    for i in range(9, -1, -1):
        if i in number_i:
            king = i
            break
    # 왕을 기준으로 구역을 나누면서 몇 명인지 셉니다.
    king_num = 0
    king_index_list = [-1]
    for i, c in enumerate(number_i):
        if c == king:
            king_num += 1
            king_index_list.append(i)
    king_index_list.append(number_len)
    # 왕의 수가 n-k보다 많거나 같으면 "왕" * (n-k) 가 답입니다.
    remain = number_len - k
    if king_num >= remain:
        return str(king)*remain
    remain -= king_num
    # 뒤에서부터 채웁니다.
    for i in range(len(king_index_list)-1, 0, -1):
        size = king_index_list[i] - king_index_list[i-1] - 1
        if size < remain:
            remain -= size
        # 구역의 크기가 구해져야 하는 수의 갯수보다 많으면 다시 그 구역에서 위의 행위를 반복합니다.
        else:
            start = king_index_list[i-1] + 1
            end = king_index_list[i]
            front = str(king)*(i-1)
            middle = solution(number[start: end], size-remain)
            back = number[king_index_list[i]:]
            return front + middle + back

print(solution("0000", 2))