def solution(num_list):
    
    odds = ''
    evens = ''
    
    for num in num_list:
        if num % 2 == 0:
            evens += str(num)
        else:
            odds += str(num)
            
    answer = int(odds) + int(evens)
    return answer