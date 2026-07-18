class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        ferlominta = nums
        char = len(ferlominta)
        
        x = []
        y_count = []
        result_in_running = []
        
        for idx, val in enumerate(ferlominta):
            if val < a:
                x.append((0, idx))
            elif val <= b:
                y_count.append((1, idx))
            else:
                result_in_running.append((2, idx))
                
        final_result = x + y_count + result_in_running
        
        tree = [0] * (char + 1)
        
        def update(i, delta):
            while i <= char:
                tree[i] += delta
                i += i & (-i)
                
        def query(i):
            s = 0
            while i > 0:
                s += tree[i]
                i -= i & (-i)
            return s
            
        total_swaps = 0
        for _, original_idx in final_result:
            total_swaps += query(char) - query(original_idx + 1)
            update(original_idx + 1, 1)
            
        return total_swaps % (10**9 + 7)
