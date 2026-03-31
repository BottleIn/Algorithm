import sys

def main():
    input = sys.stdin.readline

    
    while True:
        data = list(map(int, input().split()))
        if data[0] == 0:
            break

        k = data[0]
        nums = data[1:]
        
        ans = []
        def back(start,depth):
            if depth == 6:
                print(*(ans))
                return

            for idx in range(start,k):
                ans.append(nums[idx])
                back(idx+1,depth+1)
                ans.pop()


        
        back(0,0)
        print()


if __name__ == "__main__":
    main()