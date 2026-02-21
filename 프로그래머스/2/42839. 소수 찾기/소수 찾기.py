from itertools import permutations
def solution(numbers):
    n = len(numbers)
    numbers = list(numbers)
    a = set()
    for i in range(1,n+1):
        for p in permutations(numbers,i):
            a.add(int("".join(p))) 
    
    answer = set()
    
    for num in a:
        
        if num == 0 or num == 1:
            continue
        if num == 2:
            answer.add(num)
            
        is_prime = True
        for x in range(2, int((num ** (1/2) + 1))):
            if num % x == 0:
                is_prime = False
                break
        if is_prime : answer.add(num)
    # print(answer)
    return len(answer)