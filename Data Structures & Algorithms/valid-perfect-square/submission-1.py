class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        l,r = 0, (num-1)

        if num == 1:
            return True

        while l<=r:
            mid = (l+r)//2
            if mid*mid < num:
                l=mid+1

            elif mid*mid>num:
                r = mid-1

            else:
                return True

        return False             
        