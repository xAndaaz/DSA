
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergesort(nums, 0, len(nums) - 1)
        return nums

    def merge(self, arr, left, mid, right):
        i, j = left, mid + 1
        temp = []
        
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= right:
            temp.append(arr[j])
            j += 1
        
        arr[left:right + 1] = temp

    def mergesort(self, arr, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        self.mergesort(arr, left, mid)
        self.mergesort(arr, mid + 1, right)
        self.merge(arr, left, mid, right)
