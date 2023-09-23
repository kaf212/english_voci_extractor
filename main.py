import csv
import os
import shutil

with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    data = []
    words = []
    for line in lines:
        data.append(line)

    for s in data:
        en = ""
        de = ""
        for i, char in enumerate(s):
            if char in ["n", "v"] and list(s)[i + 1] == " " and list(s)[i - 1] == " ":  # if there's a n, v or a with a whitespace before and after
                break
            else:
                x = True
                en += char

            if char == "d" and list(s)[i + 1] == "j" and list(s)[i - 1] == "a":
                en = en.replace(" ad", "")
                break
            elif x is False:
                en += char

        if len(en) > 25:
            en = None
            #if input(f'English definition {en} is very long, keep? (Y/N)') == "n":
            #    en = None

        x = 0
        for i, char in enumerate(s):
            if char == "/":
                x += 1
            if char == "." and x == 2:
                x = 3
            if x == 3:
                de += char

        if de is not None:
            de = de.replace("File", "")

        for char in de:
            try:
                int(char)
            except ValueError:
                pass
            else:
                de = de.replace(char, "")

        if de.startswith(". ") or de.startswith(" ."):
            de = de[2:]

        de = de.replace("  \n", "")

        if en is not None:
            if en.endswith(" "):
                en = en[:-1]

        if en is not None:
            words.append((en, de))

if os.path.exists("./export.csv"):
    os.remove("./export.csv")

with open("export.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";")
    for pair in words:
        writer.writerow([pair[0], pair[1]])



