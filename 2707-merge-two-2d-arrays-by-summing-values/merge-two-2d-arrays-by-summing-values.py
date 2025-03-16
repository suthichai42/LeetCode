class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        values = {}
        for id, value in (nums1 + nums2):
            currentValue = values.get(id, 0)
            values[id] = currentValue + value

        return [[key, value] for key, value in sorted(values.items())]