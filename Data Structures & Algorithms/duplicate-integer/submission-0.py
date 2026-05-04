class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked = []
        for i in range(len(nums)):
            if nums[i] not in checked:
                checked.append(nums[i])
            else:
                return True
        return False