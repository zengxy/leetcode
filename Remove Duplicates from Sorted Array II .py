
class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        for num in nums:
            if i < 2 or num > nums[i-2]:
                nums[i] = num
                i += 1
        return i


if __name__ == '__main__':
    a = Solution()
    print(a.removeDuplicates([1,1,1,2,3,3,4,4,4,5,5,5]))

