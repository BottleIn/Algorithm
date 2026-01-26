from collections import deque
def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0:
        return 5 * len(cities)
    d = deque()
    low_city = []        
    save_cities = {}
    
    for x in cities:
        y = x.lower()
        save_cities[y] = False
        low_city.append(y)

    size = 0
    
                
    # print(d)
    # print(save_cities)
    # print(size)
    for city in low_city:
        if save_cities[city] == False: # miss
            #print("Miss")
            answer += 5 #miss 시간 증가
            
            if size != cacheSize: # 캐시가 여유가 있는 경우
                d.append(city)
                save_cities[city] = True
                size += 1
            
            elif size == cacheSize:  # 캐시가 full
                
                # 제일 오래된 거 deque에서 삭제 + 캐시 방문 시티 false
                bye_city = d.popleft() 
                save_cities[bye_city] = False
                
                d.append(city)
                save_cities[city] = True
            
        elif save_cities[city] == True: #hit
            #print("Hit")
            d.remove(city)
            d.append(city)
            answer +=1
        
        # print(d)
        # print(save_cities)
        # print(size)
        # print(answer)
        # print('=============')
    
    
    return answer
