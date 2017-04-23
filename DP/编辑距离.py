#coding = 'utf-8'
class Solution: 
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        # write your code here
        
        #状态定义和初始化
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
            
        m, n = len(word1)+1, len(word2)+1
        dp = [[0 for i in range(n)] for i in range(m)]
        for i in range(n):
            dp[0][i] = i
        for j in range(m):
            dp[j][0] = j
        
        #状态转移
        for i in range(1,m):
            for j in range(1,n):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] 
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    
        return dp[m-1][n-1]
        
        
