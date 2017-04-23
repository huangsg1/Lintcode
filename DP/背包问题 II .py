#coding = 'utf-8'
class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    # @return: The maximum value
    def backPackII(self, m, A, V):
        # write your code here
        
        if m == 0:
            return 0
            
        n = len(A)
        if n == 0:
            return 0
        #状态定义及初始化
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        
        #状态转移方程
        for i in range(1,n+1):
            for j in range(1,m+1):
                if j >= A[i-1]:
                    dp[i][j] = max(dp[i-1][j-A[i-1]]+V[i-1], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        
        res = 0
        for j in range(m+1):
            res = max(res, dp[-1][j])
            
        return res
