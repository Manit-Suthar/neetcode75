class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count frequency of each number -> {num: freq}
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Step 2: Create buckets where index = frequency
        # Size is len(nums) + 1 because max possible frequency is len(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)

        # Step 3: Walk backward from highest frequency to lowest and collect k items
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
    
print(Solution().topKFrequent([6,1,1,2,1,2,1,2,3,1,3,2,3,6,3],2))