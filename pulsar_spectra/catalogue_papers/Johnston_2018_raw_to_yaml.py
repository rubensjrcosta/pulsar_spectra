import json
import csv

with open("Johnston_2018_raw.tsv") as file:
    tsv_file = csv.reader(file, delimiter="\t")
    lines = []
    for line in tsv_file:
        lines.append(line)
print(lines)

pulsar_dict = {}
for row in lines:
    row = [r.strip() for r in row]
    if len(row) == 0:
        continue
    if row[0].startswith("#") or row[0].startswith("Name") or row[0] == '' or row[0].startswith('-') or row[1] == '':
        continue
    print(row)

    pulsar = row[0].strip().replace("–", "-")
    # Wrong names I found
    if pulsar == "J1105-43":
        pulsar = "J1105-4353"
    elif pulsar == "J1530-63":
        pulsar = "J1530-6343"
    elif pulsar == "J1552-62":
        pulsar = "J1551-6214"
    elif pulsar == "J1614-38":
        pulsar = "J1614-3846"
    elif pulsar == "J1705-52":
        pulsar = "J1704-5236"

    pulsar_dict[pulsar] = {
        "Frequency MHz":[1360],
        "Bandwidth MHz":[256],
        "Flux Density mJy":[round(float(row[1]),1)],
        "Flux Density error mJy":[round(float(row[1])*.2,1)]
    }

with open("Johnston_2018.yaml", "w") as cat_file:
    cat_file.write(json.dumps(pulsar_dict, indent=1))
print(pulsar_dict)