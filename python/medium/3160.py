class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ans = []
        color_balls = defaultdict(set)
        balls_colors = defaultdict(int)
        for ball, color in queries:
            if balls_colors[ball] and balls_colors[ball] != color:
                color_balls[balls_colors[ball]].remove(ball)
                
                if not color_balls[balls_colors[ball]]:
                    del color_balls[balls_colors[ball]]
            
            balls_colors[ball] = color
            color_balls[color].add(ball)

            distinct = len(color_balls)
            ans.append(distinct)
            
        return ans
