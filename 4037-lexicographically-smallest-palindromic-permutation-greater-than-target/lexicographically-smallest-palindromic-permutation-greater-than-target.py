class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
            
        odd_char = ""
        odd_count = 0
        for i in range(26):
            if cnt[i] % 2 == 1:
                odd_count += 1
                odd_char = chr(ord('a') + i)
            cnt[i] //= 2
        if odd_count > 1:
            return ""
        
        half_len = n // 2
        def make_palindrome(left_half):
            return left_half + odd_char + left_half[::-1]
        for match_len in range(half_len, -1, -1):
            temp_cnt = cnt[:]
            left_prefix = []
            possible = True
        
            for k in range(match_len):
                c_idx = ord(target[k]) - ord('a')
                if temp_cnt[c_idx] > 0:
                    temp_cnt[c_idx] -= 1
                    left_prefix.append(target[k])
                else:
                    possible = False
                    break
            
            if not possible:
                continue
            
            
            if match_len == half_len:
                pal = make_palindrome("".join(left_prefix))
                if pal > target:
                    return pal
                continue

            
            target_char_idx = ord(target[match_len]) - ord('a')
            for j in range(target_char_idx + 1, 26):
                if temp_cnt[j] > 0:
                    temp_cnt[j] -= 1
                    left_prefix.append(chr(ord('a') + j))
                    
                  
                    for rem_idx in range(26):
                        left_prefix.extend([chr(ord('a') + rem_idx)] * temp_cnt[rem_idx])
                    
                    return make_palindrome("".join(left_prefix))

        return ""