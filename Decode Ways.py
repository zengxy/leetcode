#wait to solve
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if len(s)==0:
            return 0
        elif len(s)==1:
            return 1
        else:
            if int(s[1])==0:
                return self.numDecodings(s[2:])
            if int(s[0])==1:
                return self.numDecodings(s[1:])+self.numDecodings(s[2:])
            elif int(s[0])==2:
                pass