class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        ans = []
        
        for i in range(len(s)):
            ans.append(s[i])
            
            if len(ans) >= len(part):
                if ''.join(ans[-len(part):]) == part:
                    for _ in range(len(part)):
                        ans.pop()
        
        return ''.join(ans)