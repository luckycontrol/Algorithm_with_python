class Solution:
    def search(self, nums, target) -> int:
        length = len(nums)
        
        return self.binary_search(nums, 0, length - 1, target)
        
    def binary_search(self, nums, low, high, target) -> int:
        if low > high: return -1
        
        pivot = (low + high) // 2
        if nums[pivot] == target: return pivot
        
        if target < nums[pivot]:
            return self.binary_search(nums, low, pivot - 1, target)
        else:
            return self.binary_search(nums, pivot + 1, high, target)