#FILE_IN="e193.DAT"
FILE_IN="S3021.DAT"
FILE_OUT=FILE_IN[:-3]+"scr"

with open(FILE_IN, "r") as imp:
  with open(FILE_OUT,"w") as exp:
    for x, line in enumerate(imp):
      if(x==0):
        exp.write("pline\n")
      else:
        exp.write(line.replace("   ","").replace("  ",",").replace(" -",",-"))
    exp.write("close\n")
    exp.write("enter\n")