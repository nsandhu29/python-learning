# K,N program
class Solution(object):
    def kthGrammer(self, N, K):
        if N == 1: return 0
        parent = self.kthGrammer(N-1, K//2 + K%2)
        is_kodd = K % 2 == 1
        if parent == 1:
            return 1 if is_kodd else 0
        else:
            return 0 if is_kodd else 1

sol = Solution()
sol.kthGrammer(4, 5)