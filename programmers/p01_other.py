prices = [1,2,3,2,3,5,6,2,3,4,5,2,3,42,23,1,5,3,4,2342,3,2,24,2,2,1,43]

def solution(p):
    ans = [0] * len(p)
    stack = [0]
    for i in range(1, len(p)):
        if p[i] < p[stack[-1]]:
            for j in stack[::-1]:
                if p[i] < p[j]:
                    ans[j] = i-j
                    print(f"answer[{j}] = {i} - {j} = {i-j}")
                    print(f"index:{j} value:{p[j]} removed")
                    stack.remove(j)
                else:
                    break
        print(f"index:{i} value:{p[i]} pushed")
        stack.append(i)
    values = [p[k] for k in stack]
    print(values)
    print(stack)
    for i in range(0, len(stack)-1):

        ans[stack[i]] = len(p) - stack[i] - 1


    return ans

print(solution(prices))