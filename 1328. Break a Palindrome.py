from string import ascii_lowercase as al
class Solution:
    def breakPalindrome(self, pp: str) -> str:
        pp, n = list(pp), len(pp)
        for i in range(n):
            if (pp[i] == 'a' or i == (n >> 1)) and (i < n - 1): continue
            else:
                if pp[i] == 'a':
                    pp[i] = 'b'
                else:
                    pp[i] = 'a'
                break
        s = ''.join(pp)
        if s != s[::-1]: return s
        else: return ''
