class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!= len(t):
           return False 

        countS, countT = {}, {}

        for i in range(len(s)): #as we know both of them are the same length
            countS[s[i]] = 1 + countS.get(s[i],0)  
            countT[t[i]] = 1 + countT.get(t[i],0)  #you did indexing with get by mistake, get is a function to be used with hashmaps
        for c in countS:
            if c not in countT:
                return False
            if countS[c] == countT[c]:
                continue
            else: 
                return False   
                 
        return True           


#time complexity = O(n)
# space = O(n)


    #YOU DID THE SYNTAX WRONG,      #countS(s[i]), YOU DID THIS INSTEAD OF countS[s[i]]
            # need get because what if the key doesnt exist yet? you would get a key error otherwise
      #my mistake: i did not take into account for the fact:
      #  s="jar"
      #t="jam"
      #the key r doesnt exist in countT