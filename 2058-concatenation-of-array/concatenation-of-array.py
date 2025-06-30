class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new  = []
        for i in range(2):
            for num in range(len(nums)):
                new.append(nums[num])
        
        return new