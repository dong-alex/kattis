"""
  Alex Dong
  1413809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  (KMP algorithm string matching) - https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  textLength/A

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 403.

"""


def computeLPSArray(pat, patternLength, lps):
    longest = 0  # length of the previous longest prefix suffix

    lps[0]  # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to patternLength-1
    while i < patternLength:
        if pat[i] == pat[longest]:
            longest += 1
            lps[i] = longest
            i += 1
        else:
            # if we found a prefix prior - that will be the last known pattern that we know exists
            if longest != 0:
                longest = lps[longest-1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1


def KMPSearch(pat, txt, lps):
    patternLength = len(pat)
    textLength = len(txt)
    solution = []
    j = 0  # index for pat[]
    i = 0  # index for txt[]
    while i < textLength:
        # found a matching value - increment
        if pat[j] == txt[i]:
            i += 1
            j += 1

        # completion - did we find the matched string
        if j == patternLength:
            # print("Found pattern at index " + str(i-j), "for string", pat, "in", txt, i,j) # why i-j : j is whole pattern, and i is the last spot where pattern is found i-j gives the extra index from 0 -> (i-j)
            solution.append(str(i-j))
            j = lps[j-1]

        # mismatch after j matches
        elif i < textLength and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    if len(solution) == 1 and solution[0] == 0:
        return []
    return solution

solution = []

try:
    while True:
        pattern = input()
        patternLength = len(pattern)

        # precompute the prefix for the pattern
        lps = [0 for _ in range(patternLength)]
        computeLPSArray(pattern, patternLength, lps)
        string = input()

        # input the string and see if a pattern is found
        solution.append(KMPSearch(pattern, string, lps))
        # print(string)
except EOFError:
    # print(' '.join(solution))
    for line in solution:
        print(' '.join(line))

