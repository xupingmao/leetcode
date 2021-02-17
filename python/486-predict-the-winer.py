# encoding=utf-8


"""
给定一个表示分数的非负整数数组。 玩家 1 从数组任意一端拿取一个分数，随后玩家 2 继续从剩余数组任意一端拿取分数，
然后玩家 1 拿，…… 。每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。
最终获得分数总和最多的玩家获胜。

给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。

示例 1：

输入：[1, 5, 2]
输出：False
解释：一开始，玩家1可以从1和2中进行选择。
如果他选择 2（或者 1 ），那么玩家 2 可以从 1（或者 2 ）和 5 中进行选择。如果玩家 2 选择了 5 ，那么玩家 1 则只剩下 1（或者 2 ）可选。
所以，玩家 1 的最终分数为 1 + 2 = 3，而玩家 2 为 5 。
因此，玩家 1 永远不会成为赢家，返回 False 。
示例 2：

输入：[1, 5, 233, 7]
输出：True
解释：玩家 1 一开始选择 1 。然后玩家 2 必须从 5 和 7 中进行选择。无论玩家 2 选择了哪个，玩家 1 都可以选择 233 。
     最终，玩家 1（234 分）比玩家 2（12 分）获得更多的分数，所以返回 True，表示玩家 1 可以成为赢家。
 

提示：

1 <= 给定的数组长度 <= 20.
数组里所有分数都为非负数且不会大于 10000000 。
如果最终两个玩家的分数相等，那么玩家 1 仍为赢家。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/predict-the-winner
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def PredictTheWinner(self, nums):
        # 玩家会设法利益最大化，也就是说每次玩的结果路径是确定的，只有一种可能性
        # 实际上只有第一个玩家有选择权
        def take_action(nums, is_first_person, choice, first_value, second_value):
            if len(nums) == 0:
                return first_value >= second_value

            if choice == 0:
                taken = nums[0]
                rest = nums[1:]
            else:
                taken = nums[-1]
                rest = nums[:-1]
                
            if is_first_person:
                first_value += taken
            else:
                second_value += taken
            if not take_action(rest, not is_first_person, 0, first_value, second_value):
                return False
            return take_action(rest, not is_first_person, 1, first_value, second_value)

        if not take_action(nums, True, 0, 0, 0):
            return False
        return take_action(nums, True, 1, 0, 0)


def test(input, expected):
    import time
    s = Solution()
    t1 = time.time()
    output = s.PredictTheWinner(*input)
    t2 = time.time()
    cost = (t2-t1) * 1000
    print("[INFO] input=%s, output=%s, cost=%sms" % (input, output, cost))
    if output != expected:
        raise Exception("[FAIL] input=%s, output=%s, expected=%s" % (input, output, expected))


test([[1,5,2]], False)
test([[1,5,233,7]], True)

