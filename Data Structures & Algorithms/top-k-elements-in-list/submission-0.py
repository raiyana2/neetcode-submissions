class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = {}

        output = []
        max_value = 0
        for i in range(len(nums)):
            hashmap[nums[i]]= 1 + hashmap.get(nums[i], 0)        
        
        for j in range(k):
            for key, value in hashmap.items():
                
                if key not in output:
                    if value > max_value:
                        max_value = value
                        max_key = key
            max_value = 0            
            output.append(max_key)    
        return output        