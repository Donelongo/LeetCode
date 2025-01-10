class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1 
        hash_map = {0 : nums[0]} 
        for i in range(1, len(nums)): 
            if nums[i] != nums[i-1]: 
                hash_map[idx] = nums[i] 
                idx += 1 
        for i in hash_map: 
            nums[i] = hash_map[i] 
         
        return idx