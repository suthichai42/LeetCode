class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        results = []

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
            
            if nums[i] != 0:
                results.append(nums[i]) 

        # append last number
        results.append(nums[i + 1])

        zeroCount = len(nums) - len(results)
        return results + [0] * zeroCount

        