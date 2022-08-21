class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index, smallest = -1, math.inf
        for i, (x1, y1) in enumerate(points):
            dx, dy = x - x1, y - y1
            #checking Manhattan distance for each point and saving the lowest
            if dx * dy == 0 and abs(dx + dy) < smallest:
                smallest = abs(dx + dy)
                index = i
        return index