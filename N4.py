import json

with open("C:/Users/BadRacoon/Documents\Config\civgraph.json") as read:
    data = json.load(read)
    stroka = ""
    for j in data.keys():
        stroka += j + ": " + " ".join(data[j]) + "\n\t" + "@echo " + j + "\n"
    with open("Makefile2", "w") as txt:
        txt.write(stroka)