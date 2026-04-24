from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        empty = [] # 빈 칸의 인덱스를 저장할 배열
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))

        def isValid(b, r, c, n):
            # 1. 해당 row와 col에 이미 num이 있는지 확인
            for i in range(9):
                if b[r][i] == n or b[i][c] == n:
                    return False

            boxRow = (r // 3) * 3
            boxCol = (c // 3) * 3

            # 2. 해당 3x3 박스에 num이 이미 있는지 확인
            for i in range(boxRow, boxRow + 3):
                for j in range(boxCol, boxCol + 3):
                    if b[i][j] == n:
                        return False

            return True

        # 빈 칸에 대해서만 dfs 실행
        def dfs(idx):
            # Base Case: 빈 칸을 모두 채운 경우 성공
            if idx == len(empty):
                return True
            r, c = empty[idx]

            for num in range(1, 10):
                if isValid(board, r, c, str(num)):
                    # 가능하다면 num 삽입 후, 다음 칸으로 이동하여 dfs 시작
                    board[r][c] = str(num)
                    if dfs(idx + 1):
                        return True
                    board[r][c] = "." # 성공하지 못한 경우 현재 칸을 되돌림.

            # 현재 for문을 전부 탐색했는데도 채울 수 있는 숫자가 없으면 False 반환
            return False

        dfs(0)

s = Solution()
print(s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))