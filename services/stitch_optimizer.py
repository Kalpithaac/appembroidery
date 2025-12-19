import math

def remove_jump_stitches(points, max_jump=8):
    optimized = []

    last = None
    
    for p in points:
        if last:
            dist = math.dist(last, p)
            if dist > max_jump:
                # break stitch path
                last = None
                continue
        
        optimized.append(p)
        last = p
    
    return optimized
