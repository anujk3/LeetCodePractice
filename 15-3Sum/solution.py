class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)

        result = []

        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:   # Main condition to prevent duplicates of first number
                continue

            front = i + 1
            back = len(nums) - 1
            # print i, front, back

            while front < back:
                sum = nums[i] + nums[front] + nums[back]
                if sum < 0:
                    front +=1
                elif sum > 0:
                    back -= 1
                else:
                    curr_list = [nums[i], nums[front], nums[back]]
                    result.append(curr_list)

                    while front < back and nums[front] == nums[front+1]: # Condition to prevent duplicates of second value in tuple
                        front += 1
                    while front < back and nums[back] == nums[back-1]: # Condition to prevent duplicates in third value of tuple
                        back -= 1 
                    front += 1
                    back -= 1

        return result