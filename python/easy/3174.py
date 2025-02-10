class Solution:
    def clearDigits(self, s: str) -> str:
        
        ans = list(s[0])
        for i in range(1 ,len(s)):
            if s[i].isdigit():
                ans.pop()
            else:
                ans.append(s[i])
        return ''.join(ans)

        
            