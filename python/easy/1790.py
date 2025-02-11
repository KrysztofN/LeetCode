class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff_chars = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_chars.append(s1[i])
                diff_chars.append(s2[i])
        
        if len(diff_chars) == 4 and len(set(diff_chars)) == 2:
            if diff_chars[0] == diff_chars[3] and diff_chars[1] == diff_chars[2]:
                return True
        
        elif not diff_chars:
            return True

        return False