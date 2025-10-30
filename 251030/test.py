def solution1(arr, k):
    answer = []
    # 순회
    for i in arr:
        # i 값이 answer에 들어있나?
        if i not in answer:
            answer.append(i)
            if len(answer) == k:
                return answer
        
        try:
            answer.index(i)
        except:
            answer.append(i)

    while len(answer) < k:
        answer.append(-1)
    return answer

def solution2(t, p):
    answer = 0

    for i in range(len(t) - len(p) + 1):
        a = int(t[i : i+len(p)])
        b = int(p)

        if a <= b:
            answer += 1
    return answer

def solution(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

def solution(s):
    answer = True
    an = 0
    for i in s:
        if i == '(':
            an += 1
        else :
            an -= 1
        if an < 0 :
            return False
    if an == 0 :
        return True
    else :
        return False
    
def solution(numbers):
    answer = [-1 ] * len(numbers)

    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i] < numbers[j]:
                answer[i] = numbers[j]
                break
    return answer


def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] < numbers[j]:
                answer.append(numbers[j])
                break
        if i + 1 != len(answer):
            answer.append(-1)

    return answer

def solution(stones, k):
    window = [max(stones[:k])]

    for i in range(k, len(stones) - k + 1):
        num = max(stones[i:k+i])
        window.append(num)
    return min(window)