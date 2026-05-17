class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # so count [a-z] = 1e, 1a, 1t, 1e, 1a, 1t
        # O (m*n*26) 26 is the length of the count array
        # hashmap: key would be 1e, 1a, 1t and value would be the list of strings so ["ate", "eat", "tea"]
        #mapping charaterc count of each string to list of anagrams
        res = defaultdict(list)  
        # what if count doesnt exist yet (.append(s) wont work), deafult value is a list

        for s in strs:
            count = [0]*26 # a ... z lower case Z

            for c in s:
                count[ord(c)-ord('a')] += 1
            res[tuple(count)].append(s)

                #a = 80 -> 80-80 = 0
                #b= 81 -> 81-80 = 1
        output = []
        for k in res:
            output.append(res[k])

        return output    




