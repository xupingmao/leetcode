class Solution:
    
    mappings = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    
    def list(self, d):
        if d in self.mappings:
            return self.mappings[d]
        return d
    
    def do_combination(self, lists, index, result):
        if len(lists) == index:
            return result
        list = lists[index]
        nresult = []
        for item in list:
            for v in result:
                nv = v + item
                nresult.append(nv)
        return self.do_combination(lists, index+1, nresult)
            
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        lists = list(map(lambda x: self.list(x), digits))
        result = self.do_combination(lists, 0, [''])
        return result
    
def test(digits, expected):
    s = Solution()
    v = s.letterCombinations(digits)
    print(v)
    assert v == expected, "failed"

test("", [])
test("23", ['ad', 'bd', 'cd', 'ae', 'be', 'ce', 'af', 'bf', 'cf'])
test("112", ['11a', '11b', '11c'])