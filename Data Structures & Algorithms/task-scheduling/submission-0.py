from typing import List
import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count frequency of each task
        count_map = {}
        for task in tasks:
            count_map[task] = count_map.get(task, 0) + 1
        
        # Build a max heap with negative frequencies (Python has min heap by default)
        max_heap = [-freq for freq in count_map.values()]
        heapq.heapify(max_heap)
        
        # Queue to keep tasks in cooldown: elements are tuples (freq, available_time)
        cooldown_queue = deque()
        
        time = 0
        
        while max_heap or cooldown_queue:
            time += 1
            
            if max_heap:
                # Pop the most frequent task
                freq = heapq.heappop(max_heap)
                freq += 1  # Decrement frequency (since freq is negative)
                
                if freq < 0:
                    # Add to cooldown with the time when it can be scheduled again
                    cooldown_queue.append((freq, time + n))
            
            # If a task has completed its cooldown, push it back to the heap
            if cooldown_queue and cooldown_queue[0][1] == time:
                freq_ready, _ = cooldown_queue.popleft()
                heapq.heappush(max_heap, freq_ready)
        
        return time
