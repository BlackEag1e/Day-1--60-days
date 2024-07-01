class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        l = 0
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l = 0
        r = k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l = k
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


'''
1.create left and right pointer
2.exchange the integer from both position until l>r
3.then change the position only for index less than the target
4.again change the int by changing l to target and r to last int of list
'''