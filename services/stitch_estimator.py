def estimate_stitches(points):
    total_stitches = len(points)
    density = total_stitches / 12.5

    return {
        "total_stitches": total_stitches,
        "est_time": f"{total_stitches/450:.1f} min",
        "density": density,
        "dimensions": "auto"
    }
