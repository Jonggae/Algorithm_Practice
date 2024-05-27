H, M =map(int, input().split())
time = H * 60 + M

fixTime = time-45

fixh = fixTime / 60
fixm = fixTime % 60
if fixTime<0:

    fixh = (24*60-45)/60
    fixm = fixTime %60

print(int(fixh), fixm)