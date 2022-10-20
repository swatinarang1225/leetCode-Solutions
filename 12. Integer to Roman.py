class Solution:
    def intToRoman(self, num: int) -> str:
        integer = [1, 4, 5, 9, 10, 40, 50, 90,100, 400, 500, 900, 1000]
        roman = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]
        res = ""
        i = 12
        while num:
            div = num// integer[i]
            num = num% integer[i]
            
            while div:
                res = res + roman[i]
                div -= 1
            
            i = i-1
        return res
            
        
        
        
