import sys

def solve():
    input = sys.stdin.readline
    n = int(input())
    
    ans = []
    stack = []
    cur = 1
    possible = True

    for _ in range(n):
        tmp = int(input())
        
        while cur <= tmp:
            stack.append(cur)
            ans.append("+")
            cur += 1
        
        if stack[-1] == tmp:
            ans.append('-')
            stack.pop()
        else:
            print("NO")
            possible = False
            break
    if possible:
        for x in ans:
            print(x)
    
if __name__ == "__main__":
    solve()