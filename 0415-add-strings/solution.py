class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        idx1 = len(num1) - 1
        idx2 = len(num2) - 1
        small_ascii = ord('0')  # ASCII of '0' is 48
        base = 10
        carry = 0
        result = []

        while idx1 >= 0 or idx2 >= 0:
            n1 = ord(num1[idx1]) - small_ascii if idx1 >= 0 else 0
            n2 = ord(num2[idx2]) - small_ascii if idx2 >= 0 else 0
            total = n1 + n2 + carry
            carry = total // base
            result.append(str(total % base))
            idx1 -= 1
            idx2 -= 1

        if carry:
            result.append(str(carry))

        return ''.join(reversed(result))

