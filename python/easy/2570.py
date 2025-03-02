class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hash_map = defaultdict(int)
        res = []
        for i in range(len(nums1)):
            hash_map[nums1[i][0]] += nums1[i][1]
        
        for i in range(len(nums2)):
            hash_map[nums2[i][0]] += nums2[i][1]
        
        for s in sorted(hash_map):
            res.append([s, hash_map[s]])
        return res