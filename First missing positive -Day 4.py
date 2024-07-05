class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range (len(nums)):
            if nums[i]<0:
                nums[i]=0
        for i in range (len(nums)):
            positive=abs(nums[i])
            if positive>=1 and positive<=len(nums):
                actual=positive-1
                if nums[actual]==0:
                    nums[actual]=-1*len(nums)-1
                elif nums[actual]>0:
                    nums[actual]*=-1

        for i in range (len(nums)):
            if nums[i]<0:
                continue
            else:
                return i+1
        return len(nums)+1


'''
1.first check for the negative int in the list
2.if negative exist replace it with Zero
3.then check each numbers actual index ex if num=4 then index=3
4.if the num exist within the length of list then change the int in the index to negative
5.if 0 present in the place place change the 0 to length + 1 and change it to negative
6.finally check for the positive int in the list the positve ints index+1 is the result
some corner logics
before checking the int in the list convert it into positive number to check 
if all the present int is negative in the final search then len(nums) +1 is possible output
'''