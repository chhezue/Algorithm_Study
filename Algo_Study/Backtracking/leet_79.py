from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        def dfs(r, c, index):
            # 현재 칸이 맞는 문자 아니면 실패
            if board[r][c] != word[index]:
                return False

            # 마지막 문자까지 일치하면 성공
            if index == len(word) - 1:
                return True

            visited[r][c] = True

            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]

                if 0 <= nr < rows and 0 <= nc < cols:
                    if not visited[nr][nc]:
                        if dfs(nr, nc, index + 1):
                            return True

            visited[r][c] = False
            return False

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False