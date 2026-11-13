class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = {}
        answer =[]
        
        for n in strs:
            key = "".join(sorted(n))
            if key in hashMap:
                hashMap[key].append(n)
            else:
                hashMap[key] = [n]    

        for value in hashMap.values():
            answer.append(value)

        return answer     
