#coding = 'utf-8'
#该问题有两个限制条件，一个是取出K个数，一个是目标值为Target，考虑每个数组元素的子状态，那么可构成三维的状态数组，和背包问题有类似的地方
class Solution:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
    def kSum(self, A, k, target):
        # write your code here
        
        #状态定义及初始化
        m,k,t = len(A)+1, k+1, target+1
        dp = [[[0 for i in range(t)] for j in range(k)] for x in range(m)]
        
        for i in range(m):
            dp[i][0][0] = 1
            
        #状态转移方程
        for i in range(1,m):
            for j in range(1,k):
                for x in range(1,t):
                    if x >= A[i-1]:
                        dp[i][j][x] = dp[i-1][j-1][x-A[i-1]] + dp[i-1][j][x] #是否将当前元素作为一项进行加和
                    else:
                        dp[i][j][x] = dp[i-1][j][x]
        
        #返回结果
        return dp[m-1][k-1][t-1]
