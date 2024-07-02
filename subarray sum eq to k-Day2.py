class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        a={0:1}
        s=0
        c=0
        n=len(nums)
        for i in nums:
            s+=i
            if s-k in a:
                c+=a[s-k]
            if s in a:
                a[s]+=1
            else:
                a[s]=1
        return c

'''
## used brute force methods of creating 2 loops and traversing leads to runtime error

1.create a dict with value 0 in it 
2.find the cumulative sum (CS)of the array
3.sub the CS with target(k)
4.if the CS  is already in dict inc the count value by its CS value
5.if CS present in the dict inc its key value
6.if the CS element is new assign 1 to its value
7.Return the count 
'''