import collections

mystr = sorted(input())
cnt = collections.Counter(mystr)
M = max(list(cnt.values()))

for i in range(97, 123) :
    if cnt[chr(i)] == M :
        print(chr(i), end='')
