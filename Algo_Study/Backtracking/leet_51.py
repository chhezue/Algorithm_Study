from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        path = []
        queens = [0] * n # 현재 퀸의 위치를 저장할 배열

        def dfs(r):
            if r == n:
                result.append(path[:])
                return

            for c in range(n):
                conflict = False

                # 같은 열 체크
                for prev_r in range(r):
                    if queens[prev_r] == c:
                        conflict = True
                        break

                if conflict:
                    continue

                # 대각선 체크
                for prev_r in range(r):
                    prev_c = queens[prev_r]
                    if abs(prev_r - r) == abs(prev_c - c):
                        conflict = True
                        break

                if conflict:
                    continue

                row_str = "." * c + "Q" + "." * (n - c - 1)

                path.append(row_str)
                queens[r] = c
                dfs(r + 1)
                queens[r] = 0
                path.pop()

        # 첫 번째 행부터 말을 놓는 경우의 수 검사
        dfs(0)

        return result

s = Solution()
print(s.solveNQueens(4))
print(s.solveNQueens(1))