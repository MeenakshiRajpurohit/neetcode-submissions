class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        a = 1
        b = 2

        for i in range(3, n+1):
            cur = a + b
            a = b
            b = cur
            
        return b
           
        
        