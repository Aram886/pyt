languages = ["Python", "Go", "JavaScript", "PHP", "Perl", "Swift", "Flask"]

name = input("your name: ")
chance = 3
while chance >= 0:
    print(f"{name},You have a {chance} chance")
    w = input("Input word of letter: ")

    for w in languages:
            print("Duq haxteciq")
    if w in languages:
        input("Input word of letter: ")
    if w in languages:
        input("Input word of letter: ")
        break
    else:
        print("chka nman tar")

    for i in languages:
        if w in i:
            print("Ka nman tar")
        else:
            chance = chance - 1
        