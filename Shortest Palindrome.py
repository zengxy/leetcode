from __future__ import division
from math import ceil


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        slen = s.__len__()
        centerPos = int(ceil(slen/2.0)) - 1

        while centerPos > 0:
            if s[:centerPos] == s[2*centerPos-s.__len__():centerPos-s.__len__():-1]:
                return s[-1:centerPos-slen:-1]+s[centerPos]+s[centerPos+1:]
            centerPos-=1
        return s[-1:-slen:-1]+s[0]+s[1:]


if __name__ == '__main__':
   a=Solution()
   print(a.shortestPalindrome("123456789"))
   #print(ceil(5/2))