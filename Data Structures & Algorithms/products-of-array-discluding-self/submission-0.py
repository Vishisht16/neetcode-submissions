class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        num_zeroes = 0
        for num in nums:
            if num != 0:
                total_prod *= num
            if num == 0:
                num_zeroes += 1
        
        if num_zeroes == 0:
            res = []
            for i in range(len(nums)):
                res.append(int(total_prod / nums[i]))
            return res

        if num_zeroes == 1:
            res = []
            for i in range(len(nums)):
                if nums[i] == 0:
                    res.append(total_prod)
                else:
                    res.append(0)
            return res

        for i in range(len(nums)):
            nums[i] = 0
        return nums

        
