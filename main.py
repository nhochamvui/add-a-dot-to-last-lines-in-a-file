with open("test.txt") as f_old, open("new.txt", "w") as f_new:
    for line in f_old:
        f_new.write(line.rstrip('\n')+'.\n')
f_old.close()
f_new.close()
