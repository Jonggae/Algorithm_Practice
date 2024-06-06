import sys
n, m = map(int, input().split())  # N: 음을 아는 노래, M개 맞춰야할 음들
songs = list(sys.stdin.readline().strip().split() for _ in range(n))
notes = list(''.join(sys.stdin.readline().split()) for _ in range(m))


songs_dic = {}
for song in songs:
    first_three_notes = ''.join(song[2:5])
    if first_three_notes in songs_dic:
        songs_dic[first_three_notes].append(song[1])
    else:
        songs_dic[first_three_notes] = [song[1]]


for note in notes:
    if note in songs_dic:
        if len(songs_dic[note]) == 1:
            print(songs_dic[note][0])
        else:
            print('?')
    else:
        print('!')