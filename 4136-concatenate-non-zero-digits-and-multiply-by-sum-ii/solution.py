class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        idx = [0] * (n + 1)
        val = [0] * (n + 1)
        total = [0] * (n + 1)
        pow10 = [1] * (n + 1)

        for i in range(1, n + 1):
            pow10[i] = pow10[i - 1] * 10 % MOD

        count = 0

        for i, ch in enumerate(s):
            digit = int(ch)

            if digit != 0:
                count += 1
                val[count] = (val[count - 1] * 10 + digit) % MOD
                total[count] = total[count - 1] + digit

            idx[i + 1] = count

        ans = []

        for left, right in queries:
            a = idx[left]
            b = idx[right + 1]

            if a == b:
                ans.append(0)
                continue

            length = b - a

            num = (val[b] - val[a] * pow10[length]) % MOD
            digit_sum = total[b] - total[a]

            ans.append(num * digit_sum % MOD)

        return ans
