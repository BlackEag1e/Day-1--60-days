class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i]>nums[j]:
                    nums[i], nums[j] = nums[j],nums[i]





"""
1.create a for loop to select the element in the list
2.Second for loop for traversing the list
3.compare the integer
4.if i is greater then swap the integer to get the sorted list
"""