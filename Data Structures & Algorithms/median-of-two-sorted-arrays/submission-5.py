class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # time: O(m+n) -> required O(log(min(m,n)))
        # space: O(1)
        
        m = len(nums1)
        n = len(nums2)

        mid = (m+n)//2
        isEven = False

        if (m+n) % 2 == 0:
            mid -= 1
            isEven = True

        if m == 0:
            if isEven:
                return (nums2[mid] + nums2[mid+1])/2.0
            else:
                return nums2[mid]

        if n == 0:
            if isEven:
                return (nums1[mid] + nums1[mid+1])/2.0
            else:
                return nums1[mid]

        i = 0
        j = 0

        while i < m and j < n:
            if (i+j) == mid:
                if not isEven:
                    return min(nums1[i], nums2[j])
                else:
                    m1 = min(nums1[i], nums2[j])
                    if nums1[i] <= nums2[j]:
                        if i + 1 == m:
                            m2 = nums2[j]
                        else:
                            m2 = min(nums1[i+1], nums2[j])
                    else:
                        if j + 1 == n:
                            m2 = nums1[i]
                        else:
                            m2 = min(nums1[i], nums2[j+1])
                    return (m1 + m2)/2.0
            
            cur1 = nums1[i]
            cur2 = nums2[j]

            if cur1 <= cur2:
                i += 1
            else:
                j += 1

        rem = mid - (i+j)
        if i < m:
            ind = i + rem
            if isEven:
                return (nums1[ind] + nums1[ind+1])/2.0
            else:
                return nums1[ind]

        if j < n:
            ind = j + rem
            if isEven:
                return (nums2[ind] + nums2[ind+1])/2.0
            else:
                return nums2[ind]

        return -1
