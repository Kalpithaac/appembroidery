import numpy as np

# Sample simplified DMC palette → can expand later
DMC_COLORS = [
    (255,255,255,"DMC Blanc"),
    (0,0,0,"DMC 310 Black"),
    (192,192,192,"DMC 535 Ash Gray"),
    (255,0,0,"DMC 666 Red"),
    (255,255,0,"DMC 444 Yellow"),
    (0,0,255,"DMC 820 Royal Blue"),
]

def match_dmc_colors(rgb_list):

    matched = []

    for color in rgb_list:
        r1,g1,b1 = color

        best_name = None
        min_dist = 99999

        for r2,g2,b2,name in DMC_COLORS:

            dist = np.linalg.norm(
                np.array([r1,g1,b1]) - np.array([r2,g2,b2])
            )

            if dist < min_dist:
                min_dist = dist
                best_name = name

        matched.append(best_name)

    return matched
