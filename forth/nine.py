class Solution:
    def is_palindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_original = x
        x_calculate = 0
        while x != 0:
            left = x % 10
            x = x // 10
            x_calculate = x_calculate * 10 + left
        return x_calculate == x_original

if __name__ == '__main__':
    s = Solution()

    print(s.is_palindrome(-121))