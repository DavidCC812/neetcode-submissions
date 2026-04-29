class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        max_area = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()

                if stack:
                    left_boundary = stack[-1]
                else:
                    left_boundary = -1
            
                width = i - left_boundary - 1
                area = heights[idx] * width
                max_area = max(max_area, area)

            stack.append(i)

        return max_area

