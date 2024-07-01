class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        n=len(nums)
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
            if d[i]>=(n/2):
                return i

'''
1.create a dict
2.traverse index in the list
3.for every first occurance of the int in dict increament 1
4.for the second occurence increament the value
5.the the inc reaches the half of length
6.return the value of the index
'''