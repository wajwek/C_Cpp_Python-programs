import math

def graham_scan(points):
    # Step 1: Find the point with the lowest y-coordinate.
    # In case of a tie, choose the point with the lowest x-coordinate.
    p0 = min(points, key=lambda p: (p[1], p[0]))

    # Helper function: Calculates the polar angle relative to p0
    def polar_angle(p):
        return math.atan2(p[1] - p0[1], p[0] - p0[0])

    # Helper function: Calculates the square of the distance from p0
    # (useful for points collinear with p0)
    def distance(p):
        return (p[0] - p0[0])**2 + (p[1] - p0[1])**2

    # Step 2: Sort points by polar angle.
    # Skip p0 in sorting. If angles are identical, choose the farther point.
    sorted_points = sorted([p for p in points if p != p0], key=lambda p: (polar_angle(p), distance(p)))

    # Function determining the turn direction (cross product)
    # Returns positive for left turn, negative for right, 0 if collinear
    def cross_product(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

    # Step 3: Use a stack to build the hull
    stack = [p0]
    if not sorted_points: return stack
    stack.append(sorted_points[0])

    for p in sorted_points[1:]:
        # Remove points from stack while they form a "right turn" (or straight line)
        # We always want a "left turn" which guarantees convexity
        while len(stack) > 1 and cross_product(stack[-2], stack[-1], p) <= 0:
            stack.pop()
        stack.append(p)

    return stack

# Example from the task
points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
result = graham_scan(points)
print(result)
