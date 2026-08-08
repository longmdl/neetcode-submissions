class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = sorted((val, idx) for idx, val in enumerate(nums))
    
        left, right = 0, len(nums) - 1
    
        # 2. Two-pointer search
        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
        
            if current_sum == target:
                result = [indexed_nums[left][1], indexed_nums[right][1]]
                return sorted(result)
            elif current_sum < target:
                left += 1   # Sum too small -> move left right to increase value
            else:
                right -= 1  # Sum too large -> move right left to decrease value
            
        return []