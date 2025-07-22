class Solution:
    def reverse(self,s):
        s = s.strip().split()
        word = s[::-1]
        return " ".join(word)