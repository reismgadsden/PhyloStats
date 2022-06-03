import sys
import getopt
import re
import CountTaxonomy as ct


def phylo_stats(argv):
    input_file = ""
    input_regex = r"^(.)*\.(csv|tsv)$"

    output_file = ""
    output_regex = r"^(.)*\.json$"
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["input=", "output=", "help="])
    except getopt.GetoptError:
        print("PhyloStat.py -i <inputfile.csv/.tsv> -o <outputfile.json>")
        sys.exit(2)
    if (("-i" not in argv and "--input" not in argv) ^ ("-o" not in argv and "--output" not in argv)) \
            and ("-h" not in argv and "--help" not in argv):
        print("Missing valid flags!\nValid Examples:\n\tPhyloStat.py -i <inputfile.csv/.tsv> -o <outputfile.json>\n\t" +
              "PhyloStat.py --input <inputfile.csv/.tsv> --output <outputfile.json>\n\t" +
              "PhyloStat.py -h\n\tPhyloStat.py --help")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
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

    ct.count_taxonomy(input_file=input_file, output_file=output_file)

if __name__ == "__main__":
    phylo_stats(sys.argv[1:])
