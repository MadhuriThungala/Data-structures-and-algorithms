from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        s_counts = Counter(s)

        
        def solve(i: int, counts: Counter) -> str:
            
            char = target[i]
            if counts[char] > 0:
                counts[char] -= 1
                if i + 1 < n:
                    res = solve(i + 1, counts)
                    if res != "":
                        return char + res
                counts[char] += 1  

           
            for ch_code in range(ord(target[i]) + 1, ord('z') + 1):
                c = chr(ch_code)
                if counts[c] > 0:
                    counts[c] -= 1
                   
                    suffix = []
                    for k in sorted(counts.keys()):
                        suffix.append(k * counts[k])
                    return char_at_idx + "".join(suffix) if 'char_at_idx' in locals() else c + "".join(suffix)

            return ""

    
        return solve(0, s_counts)
        