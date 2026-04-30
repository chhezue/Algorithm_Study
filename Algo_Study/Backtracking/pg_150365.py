import sys
sys.setrecursionlimit(10 ** 6)

def solution(n, m, x, y, r, c, k):
    cur_str = ''  # 하나의 경로를 담을 문자열

    # 빈 칸에 대해서만 dfs 실행
    def dfs(cur_r, cur_c, end_r, end_c, s):
        # 길이가 k를 초과하면 return
        if len(s) > k:
            return None

        # 현재 위치에서의 맨해튼 거리가 남은 이동 횟수보다 더 크다면,
        # 최단 거리로 움직여도 목적지에 도착할 수 없다는 뜻이 된다.
        manhattan = abs(cur_r - end_r) + abs(cur_c - end_c)
        remain = k - len(s)
        if manhattan > remain:
            return None
        else:
            # 남은 이동 횟수와 남은 거리의 차이는 반드시 짝수여야 한다. (왔다 갔다 해서 칸을 소모해야 하므로)
            if (manhattan - remain) % 2 == 1:
                return None

        # 도착 지점에 도착했고 길이가 5라면 후보 배열에 append
        if cur_r == end_r and cur_c == end_c and len(s) == k:
            return s

        # 미리 방향 배열을 사전순으로 정렬해두면, 답을 찾자마자 바로 반환할 수 있다.
        dr = [1, 0, 0, -1]
        dc = [0, -1, 1, 0]
        ch = ['d', 'l', 'r', 'u']

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if 1 <= nr <= n and 1 <= nc <= m:
                if len(s) + 1 <= k:
                    result = dfs(nr, nc, end_r, end_c, s + ch[i])
                    if result is not None:
                        return result
                else:
                    return None

    answer = dfs(x, y, r, c, cur_str)
    if answer is None:
        return "impossible"
    else:
        return answer

print(solution(3, 4, 2, 3, 3, 1, 5)) # dllrl
print(solution(2, 2, 1, 1, 2, 2, 2)) # dr
print(solution(3, 3, 1, 2, 3, 3, 4)) # impossible