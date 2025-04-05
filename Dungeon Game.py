class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        # Create a dp table with extra row and column filled with infinity
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        # Set the cells adjacent to the princess's room to 1
        dp[m][n - 1] = dp[m - 1][n] = 1

        # Fill the DP table from bottom-right to top-left
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                min_health_on_exit = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, min_health_on_exit - dungeon[i][j])
        
        return dp[0][0]