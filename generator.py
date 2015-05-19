import csv

datalocation = "./ICTracker/"

if datalocation == "":
    datalocation = input("Enter the path to your data: ")

outfile = []
parts = {}

with open(datalocation + 'template.txt') as template:
    for line in template:
        kv = line.split(":")
        parts[kv[0].strip()] = kv[1].strip()
outfile.append(parts["START"])

with open(datalocation + "data.csv", "r") as data:
    datareader = csv.reader(data, delimiter=",")
    headers = True
    headerlist = []
    for line in datareader:
        if headers:
            headerlist = line
            headers = False
        else:
            newstr = parts["MODULE"]
            for index,field in enumerate(headerlist):
                newstr = newstr.replace("{" + field + "}", line[index].strip())
            outfile.append(newstr)

outfile.append(parts["END"])

with open(datalocation + "output.txt", "w") as output:
    for item in outfile:
        print(item, file=output)
