# https://cp-algorithms.com/geometry/convex-hull.html
import math
from functools import cmp_to_key

def orientation(p1, p2, p3):
    val = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    if val == 0: return 0  # Collinear
    return 1 if val > 0 else -1 # Counter-clockwise or clockwise

def convex_hull_fixed(points):
    if len(points) <= 3:
        return sorted(points)

    # Find the starting point (bottom-most, then left-most)
    start_point = min(points, key=lambda p: (p[1], p[0]))
    
    # Sort all points by polar angle with respect to the starting point
    # Handle collinear points by sorting by distance from start_point
    def compare_points(p1, p2):
        o = orientation(start_point, p1, p2)
        if o == 0:
            dist1 = (start_point[0] - p1[0])**2 + (start_point[1] - p1[1])**2
            dist2 = (start_point[0] - p2[0])**2 + (start_point[1] - p2[1])**2
            # Sort closer points first
            return -1 if dist1 < dist2 else 1
        return -1 if o > 0 else 1 # Sort counter-clockwise

    sorted_points = sorted(points, key=cmp_to_key(compare_points))

    # The hull must start with the starting point
    hull = [sorted_points[0]]
    
    # The first element is always on the hull, so we start from the second element in the sorted list.
    # We will iterate through the rest of the points.
    for i in range(1, len(sorted_points)):
        p = sorted_points[i]
        
        # If the last two points on the hull and the current point form a non-CCW turn,
        # we pop the last point from the hull. This "straightens" the hull.
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        
        # Add the current point to the hull
        hull.append(p)
    
    # Final check for collinear points on the hull.
    # If the last two points and the first point are collinear,
    # the middle point should be removed (in case of `include_collinear = False`).
    if len(hull) > 2 and orientation(hull[-2], hull[-1], hull[0]) == 0:
        hull.pop()
        
    return hull