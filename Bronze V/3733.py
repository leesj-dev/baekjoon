while True:
    try:
        n, s = map(int, input().split())
    except:
        break  # txt 파일에서 읽어와야 하므로, EOF(end-of-file) Error를 고려해야 함.
    else:
        print(s // (n + 1))
