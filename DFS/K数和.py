#coding='utf-8'
class Solution:
    """
    @param A: An integer array.
    @param k: A positive integer (k <= length(A))
    @param target: Integer
    @return a list of lists of integer 
    """
    def kSumII(self, A, k, target):
        # write your code here
        self.res = []
        self.dfs(A, 0, k, target, 0, [])
        return self.res

    def dfs(self, A, index, k, target, sum, arr):
        if k == len(arr): # Done结束条件（结束条件之一：达到目标）
            if target == sum: # Done获得一个可行的结果
                self.res.append(arr[:])
            return # 返回进行兄弟节点的下一波

        if index >= len(A): #（约束条件之二：超出界限）
            return
        if sum > target: #剪枝
            return 
        
        #针对当前点进行展开探索
        arr.append(A[index])
        self.dfs(A, index+1, k, target, sum+A[index], arr) # 展开（1）
        arr.pop() #展开的时候注意针对全局的变量，或者不断累积的目标变量，或者其他兄弟节点之间不宜相互影响的变量进行影响的消除
        
        self.dfs(A, index+1, k, target, sum, arr) # 展开（2）
        
        
    
    
