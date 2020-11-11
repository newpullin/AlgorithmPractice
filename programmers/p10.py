



# Enter 하거나 Leave하면 changed

def solution(record):
    name_dict = {}
    inout_list = []  # (id, Enter=0, Leave=1)
    for r in record:
        state = r.split(" ")[0]
        uid = r.split(" ")[1]


        if state == "Enter":
            inout_list.append((uid, 0))
            name = r.split(" ")[2]
            name_dict[uid] = name
        elif state == "Leave":
            inout_list.append((uid, 1))
        else:
            name = r.split(" ")[2]
            name_dict[uid] = name

    answer = []
    for io in inout_list:
        state = "들어왔습니다." if io[1] == 0 else "나갔습니다."
        answer.append(f"{name_dict[io[0]]}님이 {state}")

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))