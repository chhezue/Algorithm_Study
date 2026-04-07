class Solution:
    def climbStairs(self, n: int) -> int:
        # 계단이 하나뿐인 경우 경우의 수는 1
        if n == 1:
            return 1

        # 1. DP 테이블 초기화
        # 문제의 범위만큼 크기를 잡고, 보통 0이나 최소/최댓값으로 채웁니다.
        dp = [0] * n

        # 2. Base Case 설정
        # 가장 작은 문제들의 답을 미리 적어둡니다. (집이 1개일 때, 0층일 때 등)
        dp[0] = 1 # 첫 번째 계단까지 오르는 경우의 수
        dp[1] = 2 # 두 번째 계단까지 오르는 경우의 수

        # 3. 점화식을 이용한 반복문 (상태 전이)
        # 작은 문제부터 시작해서 큰 문제로 확장해 나갑니다.
        for i in range(2, n):
            # 핵심 로직: dp[i]를 구하기 위해 이전의 값들(dp[i-1], dp[i-2] 등)을 활용
            dp[i] = dp[i - 1] + dp[i - 2]

        # 4. 최종 답안 반환
        # 우리가 원하는 전체 문제의 해는 보통 테이블의 마지막 칸에 있습니다.
        return dp[n - 1]

s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))