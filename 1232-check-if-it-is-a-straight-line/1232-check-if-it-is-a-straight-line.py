class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # for points being in a straight line
        # their slopes should be equal
        # so calculate slope at first 2 points and 
        # see if all the other points have the same slope wrt the first point
        # slope = y-y1/x-x1
        # so our equation (to check) becomes
        # y-y1/x-x1=y2-y1/x2-x1
        # =>(y-y1)*(x2-x1)=(y2-y1)*(x-x1)
        (x1, y1), (x2, y2) = coordinates[:2]
        for i in range(2, len(coordinates)):
            (x, y) = coordinates[i]
            if((y2 - y1) * (x - x1) != (y - y1) * (x2 - x1)):
                return False
        return True	