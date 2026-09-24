class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # binary search but O(1) space

        total = len(nums1) + len(nums2)
        left = (total + 1)//2
        right = (total + 2)//2

        def getAns(k_orig):
            i = 0
            j = 0
            m = len(nums1)
            n = len(nums2)

            k = k_orig
            ans = None

            while k > 0:
                if m == 0:
                    ans = nums2[j + k - 1]
                    break
                if n == 0:
                    ans = nums1[i + k - 1]
                    break
                if k == 1:
                    ans = min(nums1[i], nums2[j])
                    break

                mid1 = min(m, k//2)
                mid2 = min(n, k//2)

                if nums1[i + mid1 - 1] > nums2[j + mid2 - 1]:
                    n -= mid2
                    j += mid2
                    # move the index

                    k -= mid2

                else:
                    m -= mid1
                    i += mid1
                    k -= mid1
            return ans
        
        leftAns = getAns(left)
        if left == right:
            return leftAns

        rightAns = getAns(right)

        return (leftAns + rightAns)/2.0