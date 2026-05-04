class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        n = len(nums)
        for num in nums:
            frequency[num] += 1
        
        buckets = [[] for _ in range(n + 1)]
        for number, count in frequency.items():
            buckets[count].append(number)

        res = []

        for i in range(n, 0, -1):
            res.extend(buckets[i])
            if len(res) == k:
                return res



