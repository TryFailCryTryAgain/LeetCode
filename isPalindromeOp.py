class Solution(object):
    def isPalindrome(self, x):
        if x not in range(0,9):
            str_num = str(x)
            reverse_num = str_num[::-1]
            if str_num==reverse_num:
                val=True
            else:
                val=False
        else:
            val = True
        return val
        

    
solution = Solution()

# print(solution.isPalindrome(141))

print()