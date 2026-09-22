from typing import List

class ST:
    def __init__(self, nums: List[int], k: int):
        self.n = len(nums)
        self.k = k
        self.st = [[0] * (k + 1) for _ in range(self.n * 4)]
        self.build(1, 0, self.n - 1, nums, k)

    def merge(self, line1: List[int], line2: List[int], k: int) -> List[int]:
        newl = list(line1)
        # Total product remainder of the combined segment
        newl[k] = (line1[k] * line2[k]) % k
        # Prefix remainders from right child shifted by left child's total product
        for r in range(k):
            newl[(r * line1[k]) % k] += line2[r]
        return newl

    def build(self, node: int, l: int, r: int, nums: List[int], k: int):
        if l == r:
            rem = nums[l] % k
            self.st[node] = [0] * (k + 1)
            self.st[node][rem] = 1
            self.st[node][k] = rem
            return self.st[node]
        
        mid = (l + r) // 2
        lc = self.build(node * 2, l, mid, nums, k)
        rc = self.build(node * 2 + 1, mid + 1, r, nums, k)
        self.st[node] = self.merge(lc, rc, k)
        return self.st[node]

    def update(self, node: int, l: int, r: int, idx: int, val: int, k: int):
        if l == r:
            rem = val % k
            self.st[node] = [0] * (k + 1)
            self.st[node][rem] = 1
            self.st[node][k] = rem
            return self.st[node]

        mid = (l + r) // 2
        if idx <= mid:
            self.update(node * 2, l, mid, idx, val, k)
        else:
            self.update(node * 2 + 1, mid + 1, r, idx, val, k)

        self.st[node] = self.merge(self.st[node * 2], self.st[node * 2 + 1], k)
        return self.st[node]

    def query(self, node: int, l: int, r: int, ql: int, qr: int, k: int) -> List[int]:
        if ql <= l and r <= qr:
            return self.st[node]
        if l > qr or r < ql:
            line = [0] * (k + 1)
            line[k] = 1 % k
            return line
            
        mid = (l + r) // 2
        lc = self.query(node * 2, l, mid, ql, qr, k)
        rc = self.query(node * 2 + 1, mid + 1, r, ql, qr, k)
        return self.merge(lc, rc, k)

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]: 
        n = len(nums)
        st = ST(nums, k)
        res = []
        for i, val, start, x in queries:
            st.update(1, 0, n - 1, i, val, k)
            line = st.query(1, 0, n - 1, start, n - 1, k)
            res.append(line[x])
        return res