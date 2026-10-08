# --- HELPER MATHEMATICS ---
def ccw(A, B, C):
    """Checks the orientation (turn) of 3 points. Returns True if they turn left."""
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])


def intersect(s1, s2):
    """Short and clever way to detect intersection of two segments."""
    if not s1 or not s2: return False
    A, B, C, D = s1[0], s1[1], s2[0], s2[1]
    # Segments intersect if their endpoints lie on opposite sides of each other
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


def get_y(s, x):
    """Calculates the current Y height of a segment for a given sweep-line X position."""
    (x1, y1), (x2, y2) = s
    return y1 if x1 == x2 else y1 + (y2 - y1) * (x - x1) / (x2 - x1)


# --- SHAMOS-HOEY ALGORITHM ---
def shamos_hoey(segments):
    events = []
    for s in segments:
        events.extend([(s[0][0], 0, s), (s[1][0], 1, s)])
    events.sort()  # Sweep from left to right

    T = []  # Status of the sweep-line (simple list instead of a tree for simplicity)
    for x, event_type, s in events:
        if event_type == 0:  # LEFT END: Insert(T, s)
            T.append(s)
            T.sort(key=lambda seg: get_y(seg, x))  # Sort by Y at current X

            idx = T.index(s)
            above = T[idx - 1] if idx > 0 else None
            below = T[idx + 1] if idx < len(T) - 1 else None

            # Does Above(T, s) or Below(T, s) intersect s?
            if intersect(above, s) or intersect(below, s): return True

        else:  # RIGHT END: Delete(T, s)
            idx = T.index(s)
            above = T[idx - 1] if idx > 0 else None
            below = T[idx + 1] if idx < len(T) - 1 else None

            # Do Above(T, s) and Below(T, s) intersect each other?
            if intersect(above, below): return True
            T.remove(s)

    return False


# --- TEST ---
if __name__ == '__main__':
    # Note: segment points should always be given from left to right (x1 <= x2)!
    segments = [
        ((20, 20), (80, 80)),  # S1
        ((10, 50), (40, 50)),  # S3 (shield)
        ((30, 80), (90, 20))  # S2
    ]
    print("Do any segments intersect?", shamos_hoey(segments))
