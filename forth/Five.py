class Solution:
    def longest_palindrome(self, s: str) -> str:
        length = len(s)
        max_str = ''
        for i in range(length):
            max_str = self.check_one_center(i, s, max_str)
        for i in range(length - 1):
            max_str = self.check_two_center(i, i + 1, s, max_str)
        return max_str

    def check_one_center(self, center_index: int, s: str, max_str: str) -> str:
        """
        单中心回文
        :param center_index:
        :param s:
        :param max_str:
        :return:
        """
        p_left = center_index - 1
        p_right = center_index + 1
        return self.check_two_center(p_left, p_right, s, max_str)

    def check_two_center(self, center_index_left: int, center_index_right: int, s: str, max_str: str) -> str:
        """
        双中心回文
        :param center_index_left:
        :param center_index_right:
        :param s:
        :param max_str:
        :return:
        """
        while center_index_left >= 0 and center_index_right < len(s):
            if s[center_index_left] == s[center_index_right]:
                center_index_left -= 1
                center_index_right += 1
                continue
            return self.get_max_str(center_index_left, center_index_right, s, max_str)
        return self.get_max_str(center_index_left, center_index_right, s, max_str)

    def get_max_str(self, center_index_left: int, center_index_right: int, s: str, max_str: str) -> str:
        if center_index_right - center_index_left - 1 > len(max_str):
            return s[center_index_left + 1: center_index_right]
        else:
            return max_str


if __name__ == '__main__':
    print(range(1))

