from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter_coords = []
        start_x, start_y = -1, -1
        for r in range(m):
            for c in range(n):
                cell = classroom[r][c]
                if cell == 'S':
                    start_x, start_y = r, c
                elif cell == 'L':
                    litter_coords.append((r, c))

        num_litter = len(litter_coords)
        if num_litter == 0:
            return 0

        target_mask = (1 << num_litter) - 1
        litter_map = {pos: i for i, pos in enumerate(litter_coords)}

        best_energy = {}

        queue = deque()
        
        initial_mask = 0
        if (start_x, start_y) in litter_map:
            initial_mask |= (1 << litter_map[(start_x, start_y)])

        queue.append((start_x, start_y, initial_mask, energy, 0))
        best_energy[(start_x, start_y, initial_mask)] = energy

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            x, y, mask, cur_energy, steps = queue.popleft()

            if mask == target_mask:
                return steps

            if cur_energy == 0:
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                
                if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != 'X':
                    next_energy = cur_energy - 1
                    cell_type = classroom[nx][ny]

                    
                    if cell_type == 'R':
                        next_energy = energy

                    next_mask = mask
                    if cell_type == 'L':
                        next_mask |= (1 << litter_map[(nx, ny)])

                    
                    state_key = (nx, ny, next_mask)
                    if next_energy > best_energy.get(state_key, -1):
                        best_energy[state_key] = next_energy
                        queue.append((nx, ny, next_mask, next_energy, steps + 1))

        return -1


        