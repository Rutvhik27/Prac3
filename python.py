def orientation(p, q, r):
    """
    Function to find orientation of triplet (p, q, r).
    Returns:
        0 if p, q, r are colinear
        1 if clockwise
        2 if counterclockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # colinear
    return 1 if val > 0 else 2  # clockwise or counterclockwise

def convex_hull(points):
    """
    Function to compute the convex hull of a set of points using the Graham Scan algorithm.
    """
    n = len(points)
    if n < 3:
        return None
    
    hull = []
    
    # Find the leftmost point
    l = min(range(n), key=lambda i: points[i][0])
    p = l
    q = 0
    
    while True:
        hull.append(p)
        
        q = (p + 1) % n
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i
        
        p = q
        
        if p == l:
            break
    
    return [points[i] for i in hull]

# Test the convex hull algorithm
points = [(0, 3), (2, 2), (1, 1), (2, 1),
          (3, 0), (0, 0), (3, 3), (2, 1.5)]
convex_points = convex_hull(points)
print("Convex Hull Points:")
for point in convex_points:
    print(point)

