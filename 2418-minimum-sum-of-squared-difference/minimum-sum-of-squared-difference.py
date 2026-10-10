class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        total_k = k1 + k2
        
        # Step 1: Compute absolute differences and store their frequencies
        diff_counts = [0] * 100001
        max_diff = 0
        for a, b in zip(nums1, nums2):
            d = abs(a - b)
            diff_counts[d] += 1
            if d > max_diff:
                max_diff = d
                
        # Step 2: Greedily reduce from max_diff down to 1
        curr = max_diff
        while curr > 0 and total_k > 0:
            if diff_counts[curr] == 0:
                curr -= 1
                continue
                
            count = diff_counts[curr]
            # Operations needed to bring all 'count' elements from curr down to curr - 1
            needed = count
            
            if total_k >= needed:
                total_k -= needed
                diff_counts[curr] = 0
                diff_counts[curr - 1] += count
                curr -= 1
            else:
                # We can't reduce all elements by 1, so we reduce a portion of them
                diff_counts[curr] -= total_k
                diff_counts[curr - 1] += total_k
                total_k = 0
                break
                
        # Step 3: Calculate the final sum of squared differences
        ans = 0
        for d in range(curr + 1):
            if diff_counts[d] > 0:
                ans += diff_counts[d] * (d ** 2)
                
        # If there are any leftover operations beyond reaching 0, they can't reduce 0 further
        return ans