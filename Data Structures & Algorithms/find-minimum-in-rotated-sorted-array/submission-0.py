class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if it;s an empty list
        if not nums:
            return
        
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            # If mid element is greater than the right element,
            # the minimum is in the r half
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                # Minimum is in left half
                r = mid
        
        # When l == r, we found the minimum
        return nums[l]

