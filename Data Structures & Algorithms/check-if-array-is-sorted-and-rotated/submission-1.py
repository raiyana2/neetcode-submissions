class Solution:
    def check(self, nums: List[int]) -> bool:

        pivotIdx = 0
        for i in range(len(nums)-1):

            if nums[i] > nums[i+1]:
                pivotIdx = i+1

                break  

        if pivotIdx == 0:
            return True


        if nums[-1] > nums[pivotIdx -1] or nums[0] < nums[-1]:
            return False

        for i in range(pivotIdx, len(nums)-1):

            if nums[i] > nums[i+1]:
                return False
    


        return True              

