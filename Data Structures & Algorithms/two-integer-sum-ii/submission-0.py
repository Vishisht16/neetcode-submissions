class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:
            return [0, 1]

        i = 0
        j = i + 1
        while (numbers[i] + numbers[j]) != target:
            if numbers[i] + numbers[j] > target:
                i += 1
                j = i + 1
            else:
                j += 1
        
        return [i + 1, j + 1]
            