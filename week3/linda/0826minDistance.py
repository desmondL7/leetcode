class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1)+1, len(word2)+1
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = i
        for j in range(n):
            dp[0][j] = j
        for i in range(1, m):
            for j in range(1, n):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    replace = dp[i-1][j-1]+1
                    insert = dp[i-1][j]+1
                    delete = dp[i][j-1]+1
                    dp[i][j] = min(replace, insert, delete)
        return dp[m-1][n-1]

Solution().minDistance('hello','hi')

