class Solution:
    def intToRoman(self, num: int) -> str:
        table = [
         [1000, "M"], [900, "CM"], [500, "D"], [400, "CD"],
         [ 100, "C"], [ 90, "XC"], [ 50, "L"], [ 40, "XL"], 
         [  10, "X"], [  9, "IX"], [  5, "V"], [  4, "IV"], 
         [   1, "I"]
        ] 
        
        index = 0
        roman = ''
        while num > 0:
          if num >= table[index][0]:
            roman += table[index][1]
            num -= table[index][0]
          else:
            index += 1
        return roman