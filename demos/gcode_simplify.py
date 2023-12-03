
import sys

sys.path.append("/home/bertrand/important/prog_hop/HI_100_text_extractor")
import lib_logstudy

def usage():
    msg = """usage :
gcode_simplify <input_file> <output_file>
    """
    print(msg)

usage()

if len(sys.argv)>1:
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        output_file = None
    elif len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]


    else:
        usage()
else:
    input_file = "drawing_etiq.gcode"
    output_file = "drawing_etiq_corr.gcode"

AA = lib_logstudy.TextManipulator(input_file)
AA.remove_carriage_return()
AA.remove_regex("G00 S1.*")
AA.remove_regex("G00 E0.*")
AA.remove_regex("G01 S1.*")
AA.remove_regex("G01 E0.*")
for lettre in list("XYZ"):
    AA.replace_regex("G28 "+lettre, "G28 "+lettre+"0")

# J'enlève les F1200.0 et F300
AA.replace_regex("G91 G0  Z0.000", "G91 G0  Z1.000")
AA.replace_regex(r"F\d{4}\.\d","")
AA.replace_regex(r"F\d{3}\.\d","")
AA.replace_regex("G01", "G0")

# AA.replace_regex("")
AA.cat(quiet=True)
if output_file:
    AA.writeFile(output_file,quiet=True)



