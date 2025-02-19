
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        l, r, cnt = 0, 0, 0
        maxLen = 10**9
        sIndex = n
        Hash = [0]*256

        for c in t:
            Hash[ord(c)] += 1
        
        while(r < n):
            if Hash[ord(s[r])] > 0: cnt += 1
            Hash[ord(s[r])] -= 1
            while(cnt == m):
                if (r-l+1) < maxLen:
                    maxLen = r -l+1
                    sIndex = l
                Hash[ord(s[l])] += 1
                if Hash[ord(s[l])] > 0: cnt -= 1
                l += 1
            r += 1
        return s[sIndex:sIndex+maxLen]