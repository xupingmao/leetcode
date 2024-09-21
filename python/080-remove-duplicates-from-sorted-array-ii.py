from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        prev_num = nums[0]
        # 结果的索引
        index = 1
        total_count = 1
        repeat_count = 0

        while index < len(nums):
            item = nums[index]
            if repeat_count > 0:
                nums[index-repeat_count] = nums[index]

            if item == prev_num:
                # 第二次个重复
                total_count += 1
                diff_index = index + 1
                repeat_item = item
                while diff_index < len(nums):
                    # 第N个重复(N>2)
                    item = nums[diff_index]
                    if item != prev_num:
                        break
                    else:
                        repeat_count += 1
                    diff_index += 1

                prev_num = repeat_item
                index = diff_index
            else:
                prev_num = item
                total_count += 1
                index += 1
        
        return total_count

def run_test(input: list, expect: list):
    input_copy = input[:]
    solution = Solution()
    n = solution.removeDuplicates(input)
    print(f"{input_copy} -> {input[:n]}, expect {expect}")
    assert input[:n] == expect

if __name__ == "__main__":
    run_test([1,1,1,2,2,3], [1,1,2,2,3])
    run_test([1,2,3,3,3,3,3,3,4], [1,2,3,3,4])
    run_test([1,2,2,2,2,2], [1,2,2])
