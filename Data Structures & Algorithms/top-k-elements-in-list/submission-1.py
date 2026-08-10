class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numdict = {}
        for num in nums:
            if num not in numdict:
                numdict[num] = 1
            else:
                numdict[num] += 1
        
        sorted_dict = sorted(numdict.items(), key=lambda x: x[1],  reverse=True)
        return [item[0] for item in sorted_dict[:k]]

