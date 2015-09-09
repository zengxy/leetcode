class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        length=s.__len__()
        if length==0:
            return 0
        i=1
        while i<=length:
            if s[-i]==' ':
                i+=1
            else:
                break

        if i==length+1:
            return 0

        start=i
        while i<=length:
            if s[-i]!=' ':
                i+=1
            else:
                break

        return i-start


a=Solution()
b=a.lengthOfLastWord('aaa  ')
print(b)