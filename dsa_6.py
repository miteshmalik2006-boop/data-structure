class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return [seen[comp], i]
            seen[num] = i
        return []

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    target = 6
    print(Solution().twoSum(nums, target))