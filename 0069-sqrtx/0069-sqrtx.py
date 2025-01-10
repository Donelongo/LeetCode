class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
            
        left, right = 1, x
        
        while left <= right:
            midPoint = (left + right) // 2
        
            if midPoint * midPoint == x:
                return midPoint
            elif midPoint * midPoint < x:
                left = midPoint + 1
            else:
                right = midPoint - 1
        return right 