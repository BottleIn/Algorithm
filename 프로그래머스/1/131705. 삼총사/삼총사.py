def solution(number):
    answer = 0
    for x in range(len(number)):
        for y in range(x+1,len(number)):
            for z in number[y+1:]:
                print(number[x],y,z)
                if number[x] + number[y] + z == 0:
                    answer += 1
    return answer