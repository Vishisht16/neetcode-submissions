class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sortnum = []
        buckets = [[] for i in range(n)]
        for num in nums:
            index = int(num % n)
            buckets[index].append(num)
        for bucket in buckets:
            bucket.sort()
            sortnum.extend(bucket)

        j = -1
        key = sortnum[j]
        ans = [key]

        while len(ans) < k:
            j -= 1
            if sortnum[j] < key:
                key = sortnum[j]
                ans.append(key)

        return ans



        
        

