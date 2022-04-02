class solution():
    def findNLen(self, s: str, n: int):
        i = 0
        j = 1
        di = {}
        while j < len(s):
            if s[i] not in di:
                di[s[i]] = 1
            if s[i] == s[j]:
                di[s[i]] += 1
                j += 1
            else:
                if s[j] not in di:
                    di[s[j]] = 1
                i = j
                j += 1
        print(di)
        sorted_list = sorted(di, key=lambda x: di[x])
        return sorted_list[n+1]


if __name__ == '__main__':
    print(solution().findNLen('AAAAHHHBBCDEFFFFFF', 4))
