filePath = input("Input path")
with open(filePath,"r") as f:
    print(min([x for x in list(map(float,f.readline().split())) if x>0]))