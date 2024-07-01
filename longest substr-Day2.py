class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=set()
        l=0
        res=0
        for i in range(0,len(s)):
            while s[i] in a:
                a.remove(s[l])
                l+=1
            a.add(s[i])
            res=max(res,i-l+1)
        return res


'''
1.create a set and assign a left pointer
2.traverse i from 0 to length of string
3.if the char(i) is new then add to the set
4.if the duplicate occur remove the same char from set
5. return the result
'''
