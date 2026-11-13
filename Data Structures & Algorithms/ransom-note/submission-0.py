class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap1 = {}
        hashMap2 = {}
        for char in magazine:
            if char in hashMap1:
                hashMap1[char] += 1
            else:    
                hashMap1[char]=1
        
        for char in ransomNote:
            if (char in hashMap1) and hashMap1[char]>0:
                hashMap1[char] -= 1
                continue
            return False

        return True