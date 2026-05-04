class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_in = None
        n = len(nums)
        res = [0] * n
        prod = 1
        zeroes = 0

        for i in range(n):
            if nums[i] == 0:
                zeroes += 1

                if zeroes > 1:
                    return res

                zero_in = i
                continue

            prod *= nums[i]

        if zeroes == 1:
            res[zero_in] = prod
            return res

        for i in range(n):
            res[i] = int(prod / nums[i])
        
        return res



    