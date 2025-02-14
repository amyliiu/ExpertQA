import json


x = open("test.txt", "r")
y = open("train.txt", "r")
z = open("validation.txt", "r")

indexes = ["id", "SMILES", "description"]

num_chars = 400

output = open("output.jsonl", "w")
first_line = True
for line in x:
    if(first_line):
        first_line = False
        continue
    line = line.split("\t")
    if(len(line[2])>num_chars):
        entry = {
            "id": line[0],
            "SMILES": line[1],
            "description": "\n".join(line[2].split("."))
        }
        output.write(json.dumps(entry, ensure_ascii=False) + '\n') 

x.close()

first_line = True
for line in y:
    if(first_line):
        first_line = False
        continue
    line = line.split("\t")
    if(len(line[2])>num_chars):
        entry = {
            "id": line[0],
            "SMILES": line[1],
            "description": "\n".join(line[2].split("."))
        }
        output.write(json.dumps(entry, ensure_ascii=False) + '\n') 
y.close()

first_line = True       
for line in z:
    if(first_line):
        first_line = False
        continue
    line = line.split("\t")
    if(len(line[2])>num_chars):
        entry = {
            "id": line[0],
            "SMILES": line[1],
            "description": "\n".join(line[2].split("."))
        }
        output.write(json.dumps(entry, ensure_ascii=False) + '\n') 
z.close()




