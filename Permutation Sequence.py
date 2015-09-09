import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numList=list(range(1,n+1))
        s = self.recursionSolution(numList,n,k-1)
        return s

    def recursionSolution(self,numList,listLen,k):
        if listLen == 1:
            return str(numList[0])
        else:
            #加上int才能通过，不知为何
            thisPos = int(math.floor(k/(math.factorial(listLen-1))))
            nextK = k%math.factorial(listLen-1)
            charNow = str(numList[thisPos])
            del numList[thisPos]
            return charNow+self.recursionSolution(numList,listLen-1,nextK)

if __name__ == '__main__':
    a = Solution()
    for i in range(1,121):
        print(a.getPermutation(5,i))


