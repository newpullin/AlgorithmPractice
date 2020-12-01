from queue import PriorityQueue

def solution(jobs):
    jobs = sorted(jobs)
    n = len(jobs)
    clock = 0
    total_response_time = 0
    working_queue = PriorityQueue()
    already = 0
    while True:
        for j in range(already, n):
            if jobs[j][0] <= clock:
                working_queue.put((jobs[j][1], jobs[j][0]))
                already += 1
            else:
                break

        if working_queue.empty():
            if already == n:
                break
            clock += 1
        else:
            job_done = working_queue.get()
            clock += job_done[0]
            total_response_time += clock - job_done[1]

    return int(total_response_time/n)

test_case = [[0,20],[3,4],[3,5], [17,2]]

print(solution(test_case))