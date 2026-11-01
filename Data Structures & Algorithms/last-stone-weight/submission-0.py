class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        diff = []
        while len(stones) > 1:
            stones.sort()
            
            a = stones.pop()
                
            b = stones.pop()

            diff = a - b
                
            
            if diff > 0:
               stones.append(diff)
            
        if not stones:
                return 0
        else:
                return stones[0]
               

        