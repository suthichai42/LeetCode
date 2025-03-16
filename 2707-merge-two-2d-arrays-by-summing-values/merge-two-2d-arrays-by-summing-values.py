class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        if len(nums1) < len(nums2):
            minArrays = nums1
            maxArrays = nums2
        else:
            minArrays = nums2
            maxArrays = nums1

        values = {}
        for id, value in minArrays:
            values[id] = value

        for id, value in maxArrays:
            currentValue = values.get(id, 0)
            values[id] = currentValue + value

        return [[key, value] for key, value in sorted(values.items())]