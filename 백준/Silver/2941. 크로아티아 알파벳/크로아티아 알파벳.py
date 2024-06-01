word = input()

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# 크로아티아 문자를 발견하면 *로 치환 후 마지막 길이 측정
# 변경은 한번에 하나씩 

length = len(word)
for c in croatia:   
    word = word.replace(c,"*")
print(len(word))