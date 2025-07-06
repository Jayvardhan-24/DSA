class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxcount = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                if maxcount < count:
                    maxcount = count
                count = 0

        if count != 0 and maxcount < count:
            maxcount = count
        return maxcount

        # for i in range(0, len(nums)):
        #     if nums[i] == 1:
        #         count += 1
        #     else:
        #         if maxcount < count:
        #             maxcount = count
        #         count = 0
        #     maxi = max(count, maxcount)

        # return maxi