#coding = 'utf-8'
class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        if not s1:
            return s2==s3
        if not s2:
            return s1==s3
        if len(s3) != (len(s1)+len(s2)):
            return False
        
        #状态定义及初始化
        m, n = len(s1)+1, len(s2)+1
        dp = [[False for i in range(n)] for j in range(m)]
        dp[0][0] = True
        for i in range(1,m):
            if s3[i-1] == s1[i-1]:
                dp[i][0] = True
            else:
                break
        for j in range(1,n):
            if s3[j-1] == s2[j-1]:
                dp[0][j] = True
            else:
                break
        
        #状态转移方程
        for i in range(1,m):
            for j in range(1,n):
                if s1[i-1]==s2[j-1] and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                elif s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i-1][j] 
                elif s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = False
        
        return dp[m-1][n-1]
