def solution(tickets):
    tickets.sort()

    used = [False] * len(tickets)
    n = len(tickets)

    answer = ["ICN"]

    def dfs(path):
        if len(path) == n + 1:
            return path

        cur = path[-1] # 이후 나아가야 할 곳

        for i in range(n):
            if not used[i] and tickets[i][0] == cur:
                used[i] = True
                result = dfs(path + [tickets[i][1]])
                if result:  # 유효 경로가 있으면 바로 return
                    return result
                used[i] = False

        return []

    return dfs(answer)
