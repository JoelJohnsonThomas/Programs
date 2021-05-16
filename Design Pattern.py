for i in range(4):
    for j in range(4):
        if i == 1 | i == 4 | j == 1 | j == 4:
            print(" # ")
        else:
            print(" ",end="")
        print()
