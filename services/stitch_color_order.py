def assign_points_to_colors(points, color_names):

    color_groups = {}

    for i,c in enumerate(color_names):
        color_groups[c] = []

        # every i'th point assigned to color
        for idx,p in enumerate(points):
            if idx % len(color_names) == i:
                color_groups[c].append(p)

    return color_groups
