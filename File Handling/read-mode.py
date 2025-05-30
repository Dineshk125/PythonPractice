with open("file.txt", "r") as f:
    # for line in f:
    #     print(line)
    x = f.read()
    for ch in x:
        print(ch)
