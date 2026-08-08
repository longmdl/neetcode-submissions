class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            num_dict[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_dict and num_dict[complement] != i:
                return [i, num_dict[complement]]