import sys
import json


def count_taxonomy(input_file, output_file):

    seperator = ""
    count_dict = dict()

    tax_order = {
        1: "Kingdom",
        2: "Phylum",
        3: "Class",
        4: "Order",
        5: "Family",
        6: "Genus",
        7: "Species"
    }

    if input_file[len(input_file) - 4:] == ".csv":
        seperator = ","
    else:
        seperator = "\t"
    in_file = open(input_file, "r")
    lines = in_file.readlines()

    total_count = len(lines) - 1

    for line in lines[1:]:
        tax_column = line.split(seperator)[-1]
        taxonomy = tax_column.split(";")
        i = 0
        target = [count_dict]
        while i < len(taxonomy):
            tax = taxonomy[i].strip("\n")
            if tax not in target[0].keys():
                target[0][tax] = dict()
                target = [target[0][tax]]
                target[0]["count"] = 1
                target[0]["percent"] = 0
                target[0]["percent_total"] = (1 / total_count) * 100
                if i != len(taxonomy) - 1:
                    target[0]["Sub"] = dict()
                    target = [target[0]["Sub"]]
            else:
                target = [target[0][tax]]
                target[0]["count"] += 1
                target[0]["percent_total"] += (1 / total_count) * 100
                if i != len(taxonomy) - 1:
                    target = [target[0]["Sub"]]
            i += 1

    with open(output_file, "w") as outfile:
        json.dump(count_dict, outfile, indent=2)
    outfile.close()
    in_file.close()


if __name__ == "main":
    count_taxonomy(".\\input\\test.tsv")