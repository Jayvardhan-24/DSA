class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] != i:
        #         return i
        # return n

        # arr = list(range(0, n))
        # for i in range(len(arr)):
        #     if arr[i] not in nums:
        #         return arr[i]

        # return n

        XOR = n
        for i in range(0, n):
            XOR ^= i ^ nums[i]

        return XOR