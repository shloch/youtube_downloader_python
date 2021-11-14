with open('config.txt') as f:
    lines = f.readlines()
    print(lines)
    for url in lines:
        print(url)