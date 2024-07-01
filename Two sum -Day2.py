class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        sum=0
        while l<len(nums)-1:
            if l!=r:
                sum=nums[l]+nums[r]
                if sum==target:
                    return [l,r]
                else:
                    r-=1

            else:
                l+=1
                r=len(nums)-1
                sum=nums[l]+nums[r]
                if sum==target:
                    return [l,r]
                else:
                    r-=1



'''
1.create two pointers left and right
2.add the int in the left index plus right index and check the target
3.if the conditions fails dec r , add the int and check until l==r
4.then inc l to 1 and start to traverse  r from end by decrementing and check the target
5.if the target is met print the index of l and r in a list
'''