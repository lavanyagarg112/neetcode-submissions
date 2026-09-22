class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        m = len(nums1)
        n = len(nums2)

        mid = (m+n)//2
        isEven = False

        if (m+n) % 2 == 0:
            mid -= 1
            isEven = True

        print(mid, isEven)

        i = 0
        j = 0

        while i < m and j < n:
            print(i, j)
            if (i+j) == mid:
                if not isEven:
                    return min(nums1[i], nums2[j])
                else:
                    m1 = min(nums1[i], nums2[j])
                    if nums1[i] <= nums2[j]:
                        m2 = min(nums1[i+1], nums2[j])
                    else:
                        m2 = min(nums1[i], nums2[j+1])
                    return (m1 + m2)/2.0
            
            cur1 = nums1[i]
            cur2 = nums2[j]

            if cur1 <= cur2:
                i += 1
            else:
                j += 1

        while i < m:
            if (i+j) == mid:
                if not isEven:
                    return min(nums1[i], nums2[j])
                else:
                    m1 = min(nums1[i], nums2[j])
                    m2 = nums1[i+1]
                    return (m1 + m2)/2.0

        while j < n:
            if (i+j) == mid:
                if not isEven:
                    return min(nums1[i], nums2[j])
                else:
                    m1 = min(nums1[i], nums2[j])
                    m2 = nums2[j+1]
                    return (m1 + m2)/2.0

        return -1
