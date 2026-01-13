import math

# print(square(3))
def solution(num_list):
    multiples = 1
    squares = 0
    for x in num_list:
        multiples *= x
        squares += x
    # print(multiples, squares)
    return 1 if multiples < (squares * squares) else 0