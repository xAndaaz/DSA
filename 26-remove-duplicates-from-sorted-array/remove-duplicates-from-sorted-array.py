class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = list(set(nums))
        temp.sort()
        nums[:] = temp
        k = len(nums)
        return k