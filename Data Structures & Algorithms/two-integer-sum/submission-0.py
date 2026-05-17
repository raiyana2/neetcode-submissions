
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        My_list = []
        for i in range(len(nums)):
            hashMap[nums[i]] = i

        for j in range(len(nums)):
                if (target-nums[j]) in hashMap:
                    if j != hashMap[target-nums[j]]:
                        My_list.append(j)
                        My_list.append(hashMap[target-nums[j]])
                        return My_list

        