from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        n = len(nums)

        values = [0] * (n + 1)

        for num in freq.keys():
            if values[freq[num]] == 0:
                values[freq[num]] = [num]
            else:
                values[freq[num]].append(num)

        res = []

        for i in range(n, 0, -1):
            if values[i] == 0:
                continue
            else:
                res.extend(values[i])
                k -= len(values[i])

                if k == 0:
                    break

        return res



        
        

