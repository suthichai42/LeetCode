class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        newArray = [pivot]
        nums.remove(pivot)
        pivotIndex = 0
        for i in range(len(nums)):
            if nums[i] == pivot:
                newArray.insert(pivotIndex, nums[i])
            elif nums[i] < pivot:
                newArray.insert(pivotIndex, nums[i])
                pivotIndex += 1
            else:
                newArray.append(nums[i])

        return newArray


        