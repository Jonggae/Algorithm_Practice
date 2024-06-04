while True:
    try:
        m, n = map(int, input().split())
        print(m+n)
    except EOFError:
        break