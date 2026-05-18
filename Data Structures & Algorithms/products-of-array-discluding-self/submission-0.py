class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #without using extra memory
        result = [1] * len(nums)  #I couldnt figure out you had to initialize like this

        prefix = 1 # I didn't think of initializing prefix to 1
        for i in range(len(nums)):
            result[i] = prefix #I couldn't figure out how to traverse both ways at the same time

            prefix *= nums[i]

        postfix =1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums [i]

        return result