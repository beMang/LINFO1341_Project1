import random

with open("large_text.txt", "w") as f:
    for i in range(int(1000000*5.2)):
        f.write(str(random.randint(1000000, 1000000000)))