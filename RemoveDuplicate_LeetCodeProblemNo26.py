class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        else:
            provious_num = 0
            for current_num in range(1, len(nums)):
                if nums[current_num] != nums[provious_num]:
                    provious_num += 1
                    nums[provious_num] = nums[current_num]
            return provious_num+1