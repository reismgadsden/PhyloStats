import sys
import getopt
import re


def phylo_stats(argv):
    input_file = ""
    input_regex = r"^(.)*\.(csv|tsv)$"

    output_file = ""
    output_regex = r"^(.)*\.json$"
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["input=", "output="])
    except getopt.GetoptError:
        print("PhyloStat.py -i <inputfile.csv/.tsv> -o <outputfile.json>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("PhyloStat.py -i <inputfile.csv/.tsv> -o <outputfile.json>")
            sys.exit()
        elif opt in ("-i", "--input"):
            if re.fullmatch(input_regex, arg):
                input_file = arg
            else:
                print("Input file must be a .csv or .tsv")
                sys.exit(2)
        elif opt in ("-o", "--output"):
            if re.fullmatch(output_regex, arg):
                output_file = arg
            else:
                print("Output file must be a .json")
                sys.exit(2)
    print("Input file: " + input_file)
    print("Output file: " + output_file)

if __name__ == "__main__":
    phylo_stats(sys.argv[1:])