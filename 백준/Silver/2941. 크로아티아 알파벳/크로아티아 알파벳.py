word = input()

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

length = len(word)
for c in croatia:
   while c in word:
       word = word.replace(c,"*",1)
print(len(word))