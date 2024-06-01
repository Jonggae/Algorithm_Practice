n = int(input().strip())
playWord = [input().strip() for _ in range(n)]

m = int(input().strip())
words = [input().strip() for _ in range(m)]

# '?' 제외한 실제 사용된 단어 리스트 생성
used_words = [word for word in playWord if word != '?']

# '?'의 위치 찾기
index = playWord.index('?')

# '?' 위치에 따른 시작 문자와 끝 문자 설정
firstChar, lastChar = None, None
if index > 0:
    firstChar = playWord[index - 1][-1]  # 바로 앞 단어의 마지막 글자
if index < n - 1:
    lastChar = playWord[index + 1][0]  # 바로 뒤 단어의 첫 글자

# 조건에 맞는 단어 찾기 및 출력
found = False
for word in words:
    if word in used_words:
        continue  # 이미 사용된 단어는 건너뛰기
    if firstChar and word[0] != firstChar:
        continue  # 시작 문자가 일치해야 함
    if lastChar and word[-1] != lastChar:
        continue  # 끝 문자가 일치해야 함
    print(word)
    found = True
    break