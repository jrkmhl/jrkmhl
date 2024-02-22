class Sol:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        i = 0
        j = n

        while i < n and j >= 0:
            print("I loop ")
            print(s[i:])
            if self.checkpalindram(s, i, n):
                print(s[i:])
                return "".join(s[i:])
            print("J loop")
            print(s[0:j])
            if self.checkpalindram(s, 0, j):
                print(s[0:j])
                return "".join(s[:j])
            i += 1
            j -= 1

    def checkpalindram(self, s, start, end):
        print("Inside palindram")
        print(s[start:end])
        while start < end:
            if s[start] != s[end - 1]:
                return False
            start += 1
            end -= 1
        return True

    def generate(self):
        s = "cbbd"
        n = len(s)
        for i in range(n):
            for j in range(n - 1, -1, -1):
                print(s[i:j + 1])

    def app_possible_vovels(self, n):

        dp = [[1, 1, 1, 1, 1]]

        for i in range(1, n):
            row = [1]
            for j in range(1, 5):
                cnt = 0
                for k in range(0, j + 1):
                    cnt = cnt + dp[i - 1][k]

                row.append(cnt)
            dp.append(row)

        print(dp)

        total = 0
        for x in dp[n - 1]:
            total = total + x
        return total

    def unique_sub_str(self, s):
        n = len(s)
        max_len = 0
        char_set = set()
        i = 0
        for j in range(n):
            if s[j] not in char_set:
                char_set.add(s[j])
                max_len = max(max_len, j - i + 1)
            else:
                while s[j] in char_set:
                    char_set.remove(s[i])
                    i = i + 1
                char_set.add(s[j])

        print(max_len)


#
obj = Sol()
print(obj.longestPalindrome("babad"))

obj.unique_sub_str("pwwkew")

symble_table = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'}
