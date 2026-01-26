def solution(n, left, right):
    answer = []
    for num in range(left,right+1):
        answer.append(max(num//n,num%n)+1)
#     prev = [[0 for _ in range(n)] for _ in range(n)]
#     prev[0][0] = 1
#     x1,y1 = left // n,left % n
#     x2,y2 = right // n, right % n
    
#     x_ = max(x1,x2)
#     y_ = max(y1,y2)
#     #print(x_,y_)
    
#     for x in range(x_+1):
#         for y in range(y_+1):
#             if x==0 and y ==0:
#                 continue
#             #print(x,y)
#             if x == 0 and y != 0:
#                 prev[x][y] = prev[x][y-1] +1
#             elif y == 0 and x != 0:
#                 prev[x][y] = prev[x-1][y] + 1
#             else:
#                 prev[x][y] = prev[x-1][y-1] +1
                
#     for num in range(left,right+1):
#         answer.append(prev[num // n][num % n])
    return answer