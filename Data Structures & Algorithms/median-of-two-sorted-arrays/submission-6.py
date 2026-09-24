class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # binary search
        # k-> median??
        # see the k/2th element in both the arrays
        # the one which has the min element if k > 1 can be 
        # discarded cause then its def not k/2th element
        # and then if k==1 then take the min


        def getKthElem(A, B, m, n, i, j, k):

            # A: array 1
            # B: array 2
            # m: length of A
            # n: length of B
            # i: start index of A
            # j: start index of B

            if m > n:
                return getKthElem(B, A, n, m, j, i, k)

            if m == 0:
                return B[j + k - 1]

            if k == 1:
                return min(A[i], B[j])

            midA = min(m, k//2) # midpoint of remaining length
            midB = min(n, k//2)

            # remove B's half
            if A[i + midA - 1] > B[j + midB - 1]:
                return getKthElem(A, B, m, n - midB, i, j + midB, k - midB)

            else:
                return getKthElem(A, B, m - midA, n, i + midA, j, k - midA)

        left = (len(nums1) + len(nums2) + 1) // 2
        right = (len(nums1) + len(nums2) + 2) // 2
        if (len(nums1) + len(nums2)) % 2 != 0:
            return getKthElem(nums1, nums2, len(nums1), len(nums2), 0, 0, left)

        else:
            return (getKthElem(nums1, nums2, len(nums1), len(nums2), 0, 0, left) + getKthElem(nums1, nums2, len(nums1), len(nums2), 0, 0, right))/2.0
