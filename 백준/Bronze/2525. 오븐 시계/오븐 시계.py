A,B = map(int, input().split())
C = int(input())

time = A*60 + B
end = time + C

if end >= 24*60:
    end = end-24*60
    
endH = int(end / 60)
endM = end % 60
print(endH, endM)