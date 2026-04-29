class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        required = len(need)

        window = {}
        formed = 0
        l = 0

        best_len = float('inf')
        best_l = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in need and window[s[r]] == need[s[r]]:
                formed += 1

            while formed == required:
                current_len = r - l + 1
                if current_len < best_len:
                    best_len = current_len
                    best_l = l

                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1

        if best_len == float('inf'):
            return ""
        return s[best_l : best_l + best_len]
