class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        tree = [0] * (4 * n)

        def build(node, l, r):
            if l == r:
                tree[node] = nums[l]
                return
            mid = (l + r) // 2
            build(2 * node + 1, l, mid)
            build(2 * node + 2, mid + 1, r)
            tree[node] = tree[2 * node + 1] + tree[2 * node + 2]

        def query(node, l, r, ql, qr):
            if ql > r or qr < l:
                return 0
            if ql <= l and r <= qr:
                return tree[node]
            mid = (l + r) // 2
            return query(2 * node + 1, l, mid, ql, qr) + query(
                2 * node + 2, mid + 1, r, ql, qr
            )

        build(0, 0, n - 1)
        memo = {}

        def dfs(l, r):
            if l == r:
                return nums[l]
            if (l, r) in memo:
                return memo[(l, r)]
            left_sum = query(0, 0, n - 1, l + 1, r)
            pick_left = nums[l] - dfs(l + 1, r)
            right_sum = query(0, 0, n - 1, l, r - 1)
            pick_right = nums[r] - dfs(l, r - 1)
            memo[(l, r)] = max(pick_left, pick_right)
            return memo[(l, r)]

        return dfs(0, n - 1) >= 0