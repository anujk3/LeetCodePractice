class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        not_val = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[not_val] = nums[not_val], nums[i]
                not_val += 1
        
        nums = nums[:not_val]
        
        return not_val
        