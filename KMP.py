def KMPTable(pat):
    lps = [0] * len(pat)
    i = 1
    l = 0
    while i < len(pat):
        if pat[i] == pat[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l > 0:
                l = lps[l-1]
            else:
                lps[i] = 0  # redundant, left here for clarification
                i += 1
    return lps


def KMPSearch(str, pat):
    Ls, Lp = len(str), len(pat)
    assert Lp > 0, " The pattern is invalid"
    lps = KMPTable(pat)
    i, j = 0, 0 # i for s, j for pat

    while i < Ls:
        if str[i] == pat[j]:
            i += 1
            j += 1
            if j == Lp:
                print("Found at index %d " % (i-j))
                j = lps[j-1]
        else:
            if j > 0:
                j = lps[j-1]
            else:
                i += 1




pat = "ABABCABAB"
pat = "ABABACABAB"
pat = "AABAABAAA"
#print(KMP(pat))

s = "THIS IS A TEST TEXT"
pat = "TEST"
#pat = ""
KMPSearch(s,pat)