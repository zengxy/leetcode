class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        length=len(digits)
        for i in range(1,length+1):
            digits[-i]+=1
            if digits[-i]<=9:
                break
            else:
                digits[-i]=0
        if digits[0]==0:
            c=[1]
            c.extend(digits)
            return c
        return digits
