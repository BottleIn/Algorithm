from collections import defaultdict
def solution(sequence, k):
    answer = defaultdict(list)
    dp = [0]
    
    for x in range(1,len(sequence)+1):
        dp.append(dp[x-1] + sequence[x-1])
    left = 0
    right = 1
    min_len = 1000001
    
    while right < len(dp):
        if dp[right] - dp[left] == k:
            #print(left,right)
            min_len = min(min_len, right-left)
            if min_len not in answer:
                answer[min_len] = (left,right-1)
            #answer.append((left,right-1))
            right += 1
        elif dp[right] - dp[left] < k:
            right +=1
        else:
            left += 1
    k = min(answer)
    a,b = answer[k]    
    tmp = []
    tmp.append(a)
    tmp.append(b)
    return tmp