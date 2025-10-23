def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        dp = [1] * (n + 2)
        for i in range(2, n + 2):
            dp[i] = (dp[i - 1] * i)

        ln = 0
        rn = 0
        for k in range(n - 1):
            ln += (int(s[k]) * (dp[n - 2] // (dp[k] * (dp[n - 2 - k])))) % 10
        for k in range(1, n):
            r = k - 1
            rn += (int(s[k]) * (dp[n - 2] // (dp[r] * (dp[n - 2 - r])))) % 10

        if (ln % 10) == (rn % 10):
            return True
        else:
            return False
