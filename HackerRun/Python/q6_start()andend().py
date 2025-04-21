# Problem: https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true
import re

S = input()
K = input()

found = False
pos = 0

while pos < len(S):
    m = re.search(K, S[pos:])
    if m is None:
        break
    found = True
    print((m.start() + pos, m.end() + pos - 1))
    pos = m.start() + pos + 1
     
if not found:
    print((-1, -1))