#coding = 'utf-8'
class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
        if m == 0:
            return 0
        if not A:
            return 0
        #状态定义及初始化
        n = len(A)+1
        dp = [[False for i in range(m+1)] for j in range(2)]
        
        for i in range(2):
            dp[i][0] = True
        
        #状态转移方程
        for i in range(1, n):
            temp_i = i & 1
            temp_i2 = (i-1) & 1
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    dp[temp_i][j] = dp[temp_i2][j - A[i - 1]] or dp[temp_i2][j]
                else:
                    dp[temp_i][j] = dp[temp_i2][j]

        #输出结果
        for j in range(m + 1)[::-1]:
            if dp[temp_i][j]:
                return j
