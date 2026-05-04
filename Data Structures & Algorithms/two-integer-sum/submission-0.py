class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]

        d1 = {}

        for i in range(len(nums)):
            if (target - nums[i]) in d1.keys():
                return [d1[target - nums[i]], i]
            
            d1[nums[i]] = i