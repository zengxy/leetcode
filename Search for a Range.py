class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if len(A)==0:
            return [-1,-1]
        if len(A)==1:
            if A[0]==target:
                return [0,0]
            else:
                return [-1,-1]
        a=self.search(0,A,target)
        b=self.search(1,A,target)
        return [a,b]

    def search(self,flag,A,target):
        begin=0
        end=len(A)-1
        while(begin<end):
            temp=int((begin+end)/2)
            if A[temp]>target:
                end=temp-1
            elif A[temp]<target:
                begin=temp+1
            else:
                if flag==0:
                    if A[temp-1]!=target:
                        return temp
                    else:
                        end=temp-1
                elif flag==1:
                    if A[temp+1]!=target:
                        return temp
                    else:
                        begin=temp+1
        if A[begin]!=target:
            return -1
        return begin


a=Solution()
b=a.searchRange([1,4],4)
print(b)