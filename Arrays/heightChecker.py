from typing import List

# 11.12
def heightChecker(heights: List[int]) -> int:
    # min_r = min(heights)
    heights_raw = heights.copy()
    # swap = 0
    for w in range(len(heights)):
        r = w

        while (heights[r] > min(heights[w:])) and r < len(heights) - 1:
            # run through once to get min
            r += 1
        if r < len(heights) and w != r:
            heights[w], heights[r] = heights[r], heights[w]
            # swap += 1

        # incr and then check next min and see if the prev is repeated also store next min that is not equal to the prev min
    return sum([i != j for i, j in zip(heights, heights_raw)])
    # keep counter of how many times swapped


heights = [5, 1, 2, 3, 4]
# heights = [1, 1, 4, 2, 1, 3]

print(heightChecker(heights))
