class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        for num in nums:
            co = 0

            for i in nums:
              if i == num:
                co = co + 1
                
            if co > n/2:
                return num
            