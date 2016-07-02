class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        notzero = 0
        for i in nums:
            if i != 0:
                nums[notzero] = i
                notzero += 1
        
        for i in xrange(notzero, len(nums)):
            nums[i] = 0