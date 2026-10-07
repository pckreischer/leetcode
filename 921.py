# 921. Minimum Add to Make Parentheses Valid

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_left = 0
        open_right = 0
        for ch in s:
            if ch == '(':
                open_left += 1
            else: #ch == ')'
                if open_left > 0:
                    open_left -= 1
                else:
                    open_right += 1
        return open_left + open_right