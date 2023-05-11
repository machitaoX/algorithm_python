
class Solution(object):

    def find_diagonal_order(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m = len(mat)
        n = len(mat[0])
        length = m * n
        step = m + n - 1
        res = [0] * length
        pos = 0
        for i in range(step):
            if i % 2 == 1:
                x = 0 if i < n else i - n + 1
                y = i if i < n else n - 1
                while x < m and y >= 0:
                    res[pos] = mat[x][y]
                    pos += 1
                    x += 1
                    y -= 1
            else:
                x = i if i < m else m - 1
                y = 0 if i < m else i - m + 1
                while x >= 0 and y < n:
                    res[pos] = mat[x][y]
                    pos += 1
                    x -= 1
                    y += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.find_diagonal_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
