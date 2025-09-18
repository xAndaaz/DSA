class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n= set(nums)
        for i in range (len(nums)):
            if target - nums[i] in n and i!= nums.index(target-nums[i]):
                return (i, nums.index(target-nums[i]))    
                # break 

                