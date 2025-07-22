class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        L,R = 0,n-1
        while L<R:
            s[L],s[R] = s[R],s[L]
            L+=1
            R-=1
        