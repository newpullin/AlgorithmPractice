def solution(skill, skill_trees):
    count = 0
    for skill_tree in skill_trees:
        index = 0
        passv = True
        for se in skill_tree:
            if se in skill:
                if se == skill[index]:
                    index += 1
                else:
                    passv = False
                    break

        if passv:
            count+=1

    return count


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))