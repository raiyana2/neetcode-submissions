class Solution:
    def isPalindrome(self, x: int) -> bool:

        a = str(x)

        l,r = 0, len(a)-1

        if l == r:
            return True

        while l < r:
            if a[l] == a[r]:
                l +=1
                r -= 1
                continue
            else:
                return False

        return True