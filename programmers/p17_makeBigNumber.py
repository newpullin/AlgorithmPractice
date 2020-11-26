def solution(number, k):
    number = list(number)
    
    want_length = len(number) - k
    # 9의 개수보다 구하고자 하는 문자열 길이가 짧은 경우 처리
    # 이렇게 처리하는게 올바른건가?
    nine_num = number.count("9")
    if nine_num >= want_length:
        return "9"*want_length

    last_nine = 0
    for i in range(k):
        for c in range(last_nine, len(number)-1):
            if number[c] == '9':
                last_nine = c
                continue
            if int(number[c]) < int(number[c+1]):
                number.pop(c)
                break
        else:
            v = number.pop()

    return "".join(number)