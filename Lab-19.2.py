filePath = input("Input path")
with open(filePath, "r") as f:
    arrayOfStrings = []
    for string in f.readlines():
        if "A" in string:
            arrayOfStrings.append(string)
    print(arrayOfStrings.sort(reverse=True))
