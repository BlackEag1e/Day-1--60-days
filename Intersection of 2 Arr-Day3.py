class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=set(nums1)
        b=set(nums2)
        for i in nums1:
            if i not in a:
                a.add(i)

        for i in nums2:
            if i not in b:
                b.add(i)


        c=a.intersection(b)
        return c



'''
1.creat  a set for both array 
2.remove the duplicate and store it in the set
3.use intersection function a get the common of both a and b
4.return the output
'''