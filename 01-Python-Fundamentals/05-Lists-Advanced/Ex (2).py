# li1 = input().split(', ')
# li2 = input().split(', ')
#
# # generating words
# res = [w1
#        for w1 in li1
#        for text in li2
#        if w1 in text]
#
# # removing duplicates and printing
# print(sorted(set(), key=res.index))

li1 = input().split(', ')
li2 = input()

# generating words
substrings = [s for s in li1 if s in li2]

print(substrings)