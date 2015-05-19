import csv

outfile = []
parts = {}
with open('template.txt') as template:
    for line in template:
        kv = line.split(":")
        parts[kv[0].strip()] = kv[1].strip()
outfile.append(parts["START"])

with open("data.csv", "r") as data:
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

with open("output.txt", "w") as output:
    for item in outfile:
        print(item, file=output)
