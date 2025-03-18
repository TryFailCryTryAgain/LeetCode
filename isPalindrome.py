class Solution(object):
    def isPalindrome(self, x):

        if x < 0:
            return False

        digits = [int(a) for a in str(x)]

        i = 0
        j = len(digits) - 1

        while i < j:
            if digits[i] != digits[j]:
                return False
            i += 1
            j -= 1
        
        return True

solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(-121))
print(solution.isPalindrome(10))
        