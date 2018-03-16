class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        limit = n
        def f(n, value, gap, result):
            if n == 0:
                result.append(value)
            else:
                if value.count('(') < limit:
                    f(n-1, value + '(', gap+1, result)
                if gap > 0:
                    f(n-1, value + ')', gap-1, result)
        result = []
        f(n * 2, '', 0, result)
        return result