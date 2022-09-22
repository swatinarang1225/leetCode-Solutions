class Solution:
    def reverseWords(self, s: str) -> str:
        output = []
        input_list = list(s.split(" "))
        for i in input_list:
            output.append(i[::-1] )
        return (" ".join(output))
