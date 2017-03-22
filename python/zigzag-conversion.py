# -*- coding:utf-8 -*-  
# Created by xupingmao on 2017/03/22
# 

"""

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows 
like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

"""

import math

class Matrix:
    """矩阵的简单实现，类似于C语言的二维数组, m.get(row, col)

    """

    def __init__(self, rows, cols, init = None):
        self.rows = int(rows)
        self.cols = int(cols)
        # self.values = [init for i in range(int(cols*rows))]
        # self.values = init * int(cols*rows)
        self.values = [init] * int(cols*rows)
    
    def checkSize(self, other, msg):
        if self.cols != other.cols or self.rows != other.rows:
            raise msg + ":not the same size"

    def checkMul(self, other, msg):
        if self.cols != other.rows or self.rows != other.cols:
            raise msg + ":wrong size"

    def add(self, other):
        self.checkSize(other, "Matrix.add")
        n = Matrix(self.cols, self.rows)
        for i in range(len(self.values)):
            n.values[i] = self.values[i]+other.values[i]
        return n
    
    def sub(self, other):
        self.checkSize(other, "Matrix.sub")
        n = Matrix(self.cols, self.rows)
        for i in range(len(self.values)):
            n.values[i] = self.values[i]-other.values[i]
        return n

    def mulRow(self, other, row, col):
        sum=0
        for i in range(self.cols):
            sum+=self.get(row, i)*other.get(i, col)
        return sum
    
    def mul(self, other):
        self.checkMul(other, "Matrix.mul")
        n = Matrix(other.cols, self.rows)
        for row in range(n.rows):
            for col in range(n.cols):
                n.set(row, col, self.mulRow(other, row, col))
        return n

    def set(self, row, col, v):
        self.values[row*self.cols+col] = v
    
    def get(self, row, col):
        return self.values[row*self.cols+col]

    def __str__(self):
        lines = []
        for i in range(0, self.rows * self.cols, self.cols):
            line = self.values[i:i+self.cols]
            lines.append(str(line))
        return "\n".join(lines)



class Solution(object):

    def handleWithMatrix(self, s, numRows):
        """使用矩阵暴力解决，但是内存溢出咯"""
        cols = math.ceil(float(len(s)) / numRows / 2) * numRows
        m = Matrix(numRows, cols)
        # # 竖直方向
        direction = 1

        row = 0
        col = 0
        # # 使用状态机解决
        for i in range(len(s)):
            if row == 0:
                direction = 1
            elif row == numRows -1 :
                # 斜向
                direction = 2
            m.set(row, col, s[i])

            if direction == 1:
                row += 1
            elif direction == 2:
                col += 1
                row -= 1
        print(m)
        # for i in range(m.rows):
        #     for j in range(m.cols):
        #         v = m.get(i, j)
        #         if v:
        #             result+=v
        values = filter(None, m.values)
        return ''.join(values)

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        # return self.handleWithMatrix(s, numRows)

        # Python2的ceil返回是float
        alphaCols = int(math.ceil(float(len(s)) / numRows))
        result =[]
        for line in range(numRows):
            lines = []
            for i in range(alphaCols):
                index = i * (numRows - 1) * 2
                if line == 0 and index < len(s):
                    lines.append(s[index])
                elif line == numRows - 1:
                    index = index + numRows - 1
                    if index < len(s):
                        lines.append(s[index])
                else:
                    left = index - line
                    right = index + line
                    if left > 0 and left < len(s):
                        lines.append(s[left])
                    if right > 0 and right < len(s):
                        lines.append(s[right])
            # print(''.join(lines))
            result.append(''.join(lines))
        return ''.join(result)

        


def _convert(s, numRows):
    sol = Solution()
    actual = sol.convert(s, numRows)
    return actual

def testCase(s, numRows, expected):
    sol = Solution()
    actual = sol.convert(s, numRows)
    assert actual == expected, "expected %s but got %s" % (expected, actual)


def _test():
    """
    >>> _test()
    'OK'
    """
    testCase("PAYPALISHIRING", 1, "PAYPALISHIRING")
    testCase("PAYPALISHIRING", 2, "PYAIHRNAPLSIIG")
    testCase("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR")

    return 'OK'

# sol = Solution()
# v = sol.convert('PAYPALISHIRING', 4)
# print(v)

# import profile
# profile.run("_convert('txkrsdyronxiisbacxkdczwdlevfughpftgxzhpnuoxegagixsnbujffpcmkivbpoimnrddnrcuzdakatxcnjjsangmxbomryahpekexmyzrzjsuiwjrfduujgrkuddsfkjjwqjjoiaptulbquvxxprgvksqnwktiwefmpqczsusnfufarfxgygbjatywgthcamqpcsrumjjufpuwwteubifcbeajzhnzvdrxyismtdgbscxqyclzksdnwgzypmxlsqisaceuglvapurnyepkwuavaztqnsbhjlzjoefurcwgznwxtliqfklileyywbihmhtanywebvnakjzewjudthlenlflontbumdimcopxbrhmrlkahqwqdafphrfumgrakzmmpclttshmgsnpilgllncteipqqgschfoxjbqcuzrcrerbrzpcnrxtbpmsveudjlcsmuxitoknueonfdpsxpmaeyubepgociiqehbyxlltrbgxfypepdevdzwiqdyungksqlqnzdjqepnlpfrekwzoxwynbwjqetiuhakidtykkoxavpefngvketzfpivudgqkgasmvtygjxiemmjzuhlyakfsudoyjekrhffcydkjbsnphyrdfcciphajkojvsunbzsezyqiblvquvjxbobjdjjovzyrruettyzswraxexqyszyvnzgsirjeqjxkdbfwzeqyxqxcpnchpafcclxkdgqtpndsqkqsqgqoynsnduwsxbwznvlsbensttmkdceukuiijaxowugtxfukageeksydllpontiansizuinrcwmbdhofnslzkkcvvsmknukdpvcjdrchppiuyyalrlmbxqzsilfyhpbwmdgrwiaozjixhikawwctndoxotvvkwsxbaoyipmiaufjfqmdooybtmzhfwestwpuwfuhwi', 926)")

# profile.run("_convert('twckwuyvbihajbmhmodminftgpdcbquupwflqfiunpuwtigfwjtgzzcfofjpydjnzqysvgmiyifrrlwpwpyvqadefmvfshsrxsltbxbziiqbvosufqpwsucyjyfbhauesgzvfdwnloojejdkzugsrksakzbrzxwudxpjaoyocpxhycrxwzrpllpwlsnkqlevjwejkfxmuwvsyopxpjmbuexfwksoywkhsqqevqtpoohpd', 4)")

# _convert("0123456789ABCDEFGHIJ", 4)